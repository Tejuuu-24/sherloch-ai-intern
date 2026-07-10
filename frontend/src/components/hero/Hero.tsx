import { Sparkles, ScanFace } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Spinner } from "@/components/common/Spinner";

interface HeroProps {
  isLoading: boolean;
  onAnalyze: () => void;
}

export function Hero({ isLoading, onAnalyze }: HeroProps) {
  return (
    <section className="border-b border-border bg-gradient-to-b from-indigo-50/60 to-white">
      <div className="mx-auto flex max-w-6xl flex-col items-center gap-6 px-6 py-20 text-center">
        <span className="inline-flex items-center gap-1.5 rounded-full border border-indigo-100 bg-indigo-50 px-3.5 py-1 text-xs font-semibold text-indigo-700">
          <Sparkles className="h-3.5 w-3.5" />
          Multimodal candidate verification
        </span>

        <h1 className="max-w-3xl font-display text-4xl font-extrabold tracking-tight text-ink sm:text-5xl">
          AI Interview Candidate Identification System
        </h1>

        <p className="max-w-2xl text-balance text-base leading-relaxed text-ink-soft sm:text-lg">
          Identify the interview candidate using metadata, Vision AI,
          Whisper speech recognition, and Gemini LLM reasoning.
        </p>

        <div className="mt-4 flex flex-col items-center gap-3">
          <Button
            size="lg"
            onClick={onAnalyze}
            disabled={isLoading}
            className="min-w-64"
          >
            {isLoading ? (
              <Spinner label="Analyzing session…" tone="inverted" />
            ) : (
              <>
                <ScanFace className="h-5 w-5" />
                Analyze Candidate
              </>
            )}
          </Button>
          <p className="text-xs text-ink-muted">
            Calls <code className="font-mono-data text-[11px]">GET /identify</code> on
            your FastAPI backend
          </p>
        </div>
      </div>
    </section>
  );
}
