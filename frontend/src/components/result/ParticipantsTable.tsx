import { Trophy } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { EmptyState } from "@/components/common/EmptyState";
import { cn } from "@/lib/utils";
import type { Participant } from "@/types/candidate";

interface ParticipantsTableProps {
  participants: Participant[];
}

export function ParticipantsTable({ participants }: ParticipantsTableProps) {
  const sorted = [...participants].sort((a, b) => b.score - a.score);
  const topScore = sorted[0]?.score;

  return (
    <Card>
      <CardHeader>
        <CardTitle>Participants</CardTitle>
        <CardDescription>Ranked by identification score</CardDescription>
      </CardHeader>
      <CardContent>
        {sorted.length === 0 ? (
          <EmptyState
            title="No participants detected"
            description="The backend did not return any participant records for this session."
          />
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full border-collapse text-sm">
              <thead>
                <tr className="border-b border-border text-left text-xs font-semibold uppercase tracking-wide text-ink-muted">
                  <th className="py-2.5 pr-4">Rank</th>
                  <th className="py-2.5 pr-4">Participant</th>
                  <th className="py-2.5 pr-4">Email</th>
                  <th className="py-2.5 pr-0 text-right">Score</th>
                </tr>
              </thead>
              <tbody>
                {sorted.map((participant, index) => {
                  const isTop = participant.score === topScore;
                  return (
                    <tr
                      key={`${participant.email}-${index}`}
                      className={cn(
                        "border-b border-border last:border-0",
                        isTop && "bg-indigo-50/60",
                      )}
                    >
                      <td className="py-3 pr-4 font-mono-data text-ink-soft">
                        <span className="inline-flex items-center gap-1.5">
                          {isTop && <Trophy className="h-3.5 w-3.5 text-indigo-600" />}
                          #{index + 1}
                        </span>
                      </td>
                      <td
                        className={cn(
                          "py-3 pr-4 font-medium",
                          isTop ? "text-indigo-700" : "text-ink",
                        )}
                      >
                        {participant.display_name}
                      </td>
                      <td className="py-3 pr-4 text-ink-soft">{participant.email}</td>
                      <td className="py-3 pr-0 text-right font-mono-data font-semibold text-ink">
                        {participant.score}
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        )}
      </CardContent>
    </Card>
  );
}
