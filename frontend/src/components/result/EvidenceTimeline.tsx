import { CheckCircle2 } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { EmptyState } from "@/components/common/EmptyState";

interface EvidenceTimelineProps {
  evidence: string[];
}

export function EvidenceTimeline({ evidence }: EvidenceTimelineProps) {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Evidence Timeline</CardTitle>
        <CardDescription>Signals gathered across the identification pipeline</CardDescription>
      </CardHeader>
      <CardContent>
        {evidence.length === 0 ? (
          <EmptyState
            title="No evidence recorded"
            description="The backend did not return any supporting signals for this session."
          />
        ) : (
          <ul className="flex flex-col gap-3">
            {evidence.map((item, index) => (
              <li
                key={`${index}-${item}`}
                className="flex items-start gap-3 rounded-xl border border-border bg-surface px-4 py-3"
              >
                <CheckCircle2 className="mt-0.5 h-4 w-4 shrink-0 text-success-500" />
                <span className="text-sm text-ink-soft">{item}</span>
              </li>
            ))}
          </ul>
        )}
      </CardContent>
    </Card>
  );
}
