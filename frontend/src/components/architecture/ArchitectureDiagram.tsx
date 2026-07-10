import {
  ArrowDown,
  Database,
  Eye,
  AudioLines,
  Gauge,
  Gem,
  UserCheck,
} from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { cn } from "@/lib/utils";

const STAGES = [
  { label: "Metadata", icon: Database, description: "Display name & email extraction" },
  { label: "YOLO Vision", icon: Eye, description: "Face & camera presence detection" },
  { label: "Whisper", icon: AudioLines, description: "Speech-to-text transcription" },
  { label: "Confidence Engine", icon: Gauge, description: "Signal fusion & scoring" },
  { label: "Gemini", icon: Gem, description: "LLM reasoning over evidence" },
  { label: "Candidate Identified", icon: UserCheck, description: "Final verdict" },
] as const;

export function ArchitectureDiagram() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>How Identification Works</CardTitle>
        <CardDescription>A multimodal pipeline fuses five independent signals into one verdict</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="flex flex-col items-center gap-1 md:flex-row md:justify-between md:gap-2">
          {STAGES.map((stage, index) => {
            const Icon = stage.icon;
            const isFinal = index === STAGES.length - 1;
            return (
              <div key={stage.label} className="flex flex-col items-center md:flex-1">
                <div className="flex flex-col items-center gap-2 text-center">
                  <div
                    className={cn(
                      "flex h-14 w-14 items-center justify-center rounded-2xl border",
                      isFinal
                        ? "border-success-500/30 bg-success-50"
                        : "border-indigo-100 bg-indigo-50",
                    )}
                  >
                    <Icon
                      className={cn(
                        "h-6 w-6",
                        isFinal ? "text-success-600" : "text-indigo-600",
                      )}
                    />
                  </div>
                  <div>
                    <p className="text-sm font-semibold text-ink">{stage.label}</p>
                    <p className="max-w-[9rem] text-xs text-ink-muted">{stage.description}</p>
                  </div>
                </div>

                {!isFinal && (
                  <div className="flex h-8 items-center justify-center md:h-auto md:w-full md:flex-1">
                    <ArrowDown className="h-4 w-4 text-ink-muted md:-rotate-90" />
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </CardContent>
    </Card>
  );
}
