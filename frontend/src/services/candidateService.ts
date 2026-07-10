import axios from "axios";
import { httpClient } from "./httpClient";
//import type { IdentifyResponse } from "@/types/candidate";

/** Normalized error shape surfaced to the UI layer. */
export class IdentifyRequestError extends Error {
  readonly status?: number;

  constructor(message: string, status?: number) {
    super(message);
    this.name = "IdentifyRequestError";
    this.status = status;
  }
}

/**
 * Calls `GET /identify` on the FastAPI backend and returns the raw
 * candidate identification payload.
 *
 * Throws `IdentifyRequestError` with a human-readable message on
 * network failure, timeout, or a non-2xx response.
 */
// export async function identifyCandidate(
//   signal?: AbortSignal,
// ): Promise<IdentifyResponse> {
//   try {
//     const response = await httpClient.get<IdentifyResponse>("/identify", {
//       signal,
//     });
//     return response.data;
//   } catch (error) {
//     if (axios.isCancel(error)) {
//       throw error;
//     }

//     if (axios.isAxiosError(error)) {
//       if (error.code === "ECONNABORTED") {
//         throw new IdentifyRequestError(
//           "THIS IS A TEST MESSAGE 1234",
//         );
//       }
//       if (!error.response) {
//         throw new IdentifyRequestError(
//           "Could not reach the backend. Confirm the FastAPI server is running and reachable.",
//         );
//       }
//       throw new IdentifyRequestError(
//         error.response.data?.detail ??
//           `The backend returned an error (${error.response.status}).`,
//         error.response.status,
//       );
//     }

//     throw new IdentifyRequestError("An unexpected error occurred.");
//   }
// }
export async function identifyCandidate(signal?: AbortSignal) {
  console.log("=== identifyCandidate START ===");
  console.log("Base URL:", httpClient.defaults.baseURL);

  try {
    const response = await httpClient.get("/identify", { signal });

    console.log("SUCCESS");
    console.log(response);

    return response.data;
  } catch (error) {
    console.error("FULL ERROR:", error);

    if (axios.isAxiosError(error)) {
      console.log("code:", error.code);
      console.log("message:", error.message);
      console.log("response:", error.response);
      console.log("request:", error.request);
      console.log("config:", error.config);
    }

    throw error;
  }
}