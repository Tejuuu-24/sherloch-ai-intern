import { useCallback, useEffect, useRef, useState } from "react";
import type { IdentifyResponse } from "@/types/candidate";
import { identifyCandidate, IdentifyRequestError } from "@/services/candidateService";

type RequestStatus = "idle" | "loading" | "success" | "error";

interface UseIdentifyCandidateResult {
  status: RequestStatus;
  data: IdentifyResponse | null;
  errorMessage: string | null;
  runAnalysis: () => void;
}

/**
 * Drives the `GET /identify` request lifecycle: idle -> loading -> success/error.
 * Cancels any in-flight request if the component unmounts or a new
 * analysis is triggered before the previous one resolves.
 */
export function useIdentifyCandidate(): UseIdentifyCandidateResult {
  const [status, setStatus] = useState<RequestStatus>("idle");
  const [data, setData] = useState<IdentifyResponse | null>(null);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const controllerRef = useRef<AbortController | null>(null);

  const runAnalysis = useCallback(() => {
    controllerRef.current?.abort();
    const controller = new AbortController();
    controllerRef.current = controller;

    setStatus("loading");
    setErrorMessage(null);

    identifyCandidate(controller.signal)
      .then((result) => {
        setData(result);
        setStatus("success");
      })
      .catch((error: unknown) => {
        if (error instanceof DOMException && error.name === "AbortError") {
          return;
        }
        const message =
          error instanceof IdentifyRequestError
            ? error.message
            : "Something went wrong while analyzing the session.";
        setErrorMessage(message);
        setStatus("error");
      });
  }, []);

  useEffect(() => {
    return () => controllerRef.current?.abort();
  }, []);

  return { status, data, errorMessage, runAnalysis };
}
