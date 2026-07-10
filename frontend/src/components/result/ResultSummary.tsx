import { CheckCircle2, XCircle, Mail, UserRound } from "lucide-react";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { ConfidenceCircle } from "@/components/result/ConfidenceCircle";
import type { Candidate } from "@/types/candidate";

interface ResultSummaryProps {
  candidate: Candidate | null;
  confidence: number;
  isCandidate: boolean;
}

export function ResultSummary({ candidate, confidence, isCandidate }: ResultSummaryProps) {
  return (
    <Card className="overflow-hidden">
      <div className="grid gap-8 p-8 md:grid-cols-[1fr_auto] md:items-center">
        <div className="flex flex-col gap-5">
          <Badge tone={isCandidate ? "success" : "danger"} className="w-fit">
            {isCandidate ? (
              <CheckCircle2 className="h-3.5 w-3.5" />
            ) : (
              <XCircle className="h-3.5 w-3.5" />
            )}
            {isCandidate ? "Candidate Identified" : "Candidate Not Identified"}
          </Badge>

          <div className="flex items-center gap-4">
            <div className="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-indigo-50">
              <UserRound className="h-7 w-7 text-indigo-600" />
            </div>
            <div className="min-w-0">
              <p className="font-display text-2xl font-bold tracking-tight text-ink">
                {candidate?.display_name ?? "Unknown participant"}
              </p>
              <div className="mt-1 flex items-center gap-1.5 text-sm text-ink-soft">
                <Mail className="h-3.5 w-3.5 shrink-0" />
                <span className="truncate">{candidate?.email ?? "No email detected"}</span>
              </div>
            </div>
          </div>
        </div>

        <div className="flex justify-center md:justify-end">
          <ConfidenceCircle confidence={confidence} isCandidate={isCandidate} />
        </div>
      </div>
    </Card>
  );
}
