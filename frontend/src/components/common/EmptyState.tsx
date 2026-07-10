import { ScanSearch } from "lucide-react";

interface EmptyStateProps {
  title: string;
  description: string;
}

export function EmptyState({ title, description }: EmptyStateProps) {
  return (
    <div className="flex flex-col items-center gap-3 rounded-2xl border border-dashed border-border-strong bg-surface px-6 py-12 text-center">
      <div className="flex h-12 w-12 items-center justify-center rounded-full bg-white shadow-[var(--shadow-card)]">
        <ScanSearch className="h-6 w-6 text-ink-muted" />
      </div>
      <div className="space-y-1">
        <p className="font-display text-base font-semibold text-ink">{title}</p>
        <p className="max-w-md text-sm text-ink-muted">{description}</p>
      </div>
    </div>
  );
}
