import { useEffect, useState } from "react";
import { cn } from "@/lib/utils";

interface ConfidenceCircleProps {
  confidence: number;
  isCandidate: boolean;
}

function confidenceLabel(confidence: number): string {
  if (confidence >= 85) return "High Confidence";
  if (confidence >= 60) return "Moderate Confidence";
  return "Low Confidence";
}

const RADIUS = 70;
const CIRCUMFERENCE = 2 * Math.PI * RADIUS;

export function ConfidenceCircle({ confidence, isCandidate }: ConfidenceCircleProps) {
  const clamped = Math.max(0, Math.min(100, confidence));
  const [animatedValue, setAnimatedValue] = useState(0);

  useEffect(() => {
    const frame = requestAnimationFrame(() => setAnimatedValue(clamped));
    return () => cancelAnimationFrame(frame);
  }, [clamped]);

  const strokeColor = isCandidate ? "var(--color-success-500)" : "var(--color-danger-500)";
  const offset = CIRCUMFERENCE - (animatedValue / 100) * CIRCUMFERENCE;

  return (
    <div className="flex flex-col items-center gap-3">
      <div className="relative h-44 w-44">
        <svg viewBox="0 0 160 160" className="h-full w-full -rotate-90">
          <circle
            cx="80"
            cy="80"
            r={RADIUS}
            fill="none"
            stroke="var(--color-border)"
            strokeWidth="12"
          />
          <circle
            cx="80"
            cy="80"
            r={RADIUS}
            fill="none"
            stroke={strokeColor}
            strokeWidth="12"
            strokeLinecap="round"
            strokeDasharray={CIRCUMFERENCE}
            strokeDashoffset={offset}
            className="transition-[stroke-dashoffset] duration-1000 ease-out"
          />
        </svg>
        <div className="absolute inset-0 flex flex-col items-center justify-center">
          <span className="font-display text-4xl font-extrabold tracking-tight text-ink">
            {Math.round(animatedValue)}%
          </span>
          <span className="text-xs font-medium text-ink-muted">confidence</span>
        </div>
      </div>
      <p
        className={cn(
          "font-display text-base font-semibold",
          isCandidate ? "text-success-600" : "text-danger-600",
        )}
      >
        {confidenceLabel(clamped)}
      </p>
    </div>
  );
}
