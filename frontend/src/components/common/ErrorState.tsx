import { AlertTriangle, RotateCw } from "lucide-react";
import { Button } from "@/components/ui/button";

interface ErrorStateProps {
  message: string;
  onRetry: () => void;
}

export function ErrorState({ message, onRetry }: ErrorStateProps) {
  return (
    <div className="flex flex-col items-center gap-4 rounded-2xl border border-danger-500/20 bg-danger-50 px-6 py-10 text-center">
      <div className="flex h-12 w-12 items-center justify-center rounded-full bg-white">
        <AlertTriangle className="h-6 w-6 text-danger-600" />
      </div>
      <div className="space-y-1">
        <p className="font-display text-base font-semibold text-ink">
          Analysis failed
        </p>
        <p className="max-w-md text-sm text-ink-soft">{message}</p>
      </div>
      <Button variant="secondary" size="sm" onClick={onRetry}>
        <RotateCw className="h-3.5 w-3.5" />
        Try again
      </Button>
    </div>
  );
}
