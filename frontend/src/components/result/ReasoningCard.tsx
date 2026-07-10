import { FileText, BrainCircuit } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

interface ReasoningCardProps {
  summary: string;
  reason: string;
}

export function ReasoningCard({ summary, reason }: ReasoningCardProps) {
  return (
    <Card>
      <CardHeader>
        <CardTitle>AI Reasoning</CardTitle>
      </CardHeader>
      <CardContent className="flex flex-col gap-6">
        <div className="flex gap-3">
          <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-xl bg-indigo-50">
            <FileText className="h-4 w-4 text-indigo-600" />
          </div>
          <div>
            <p className="text-sm font-semibold text-ink">Summary</p>
            <p className="mt-1 text-sm leading-relaxed text-ink-soft">{summary}</p>
          </div>
        </div>

        <div className="flex gap-3">
          <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-xl bg-indigo-50">
            <BrainCircuit className="h-4 w-4 text-indigo-600" />
          </div>
          <div>
            <p className="text-sm font-semibold text-ink">Reason</p>
            <p className="mt-1 text-sm leading-relaxed text-ink-soft">{reason}</p>
          </div>
        </div>
      </CardContent>
    </Card>
  );
}
