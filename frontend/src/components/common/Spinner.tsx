import { Loader2 } from "lucide-react";
import { cn } from "@/lib/utils";

interface SpinnerProps {
  className?: string;
  label?: string;
  tone?: "default" | "inverted";
}

export function Spinner({ className, label, tone = "default" }: SpinnerProps) {
  return (
    <div
      className={cn(
        "flex items-center gap-2",
        tone === "inverted" ? "text-white" : "text-ink-soft",
      )}
      role="status"
      aria-live="polite"
    >
      <Loader2
        className={cn(
          "h-4 w-4 animate-spin",
          tone === "inverted" ? "text-white" : "text-indigo-600",
          className,
        )}
      />
      {label ? <span className="text-sm font-medium">{label}</span> : null}
    </div>
  );
}
