import * as React from "react";
import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "@/lib/utils";

const badgeVariants = cva(
  "inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-xs font-semibold",
  {
    variants: {
      tone: {
        neutral: "bg-surface text-ink-soft border border-border",
        indigo: "bg-indigo-50 text-indigo-700 border border-indigo-100",
        success: "bg-success-50 text-success-600 border border-success-500/20",
        danger: "bg-danger-50 text-danger-600 border border-danger-500/20",
        warning: "bg-warning-50 text-warning-500 border border-warning-500/20",
      },
    },
    defaultVariants: {
      tone: "neutral",
    },
  },
);

export interface BadgeProps
  extends React.HTMLAttributes<HTMLSpanElement>,
    VariantProps<typeof badgeVariants> {}

export function Badge({ className, tone, ...props }: BadgeProps) {
  return <span className={cn(badgeVariants({ tone }), className)} {...props} />;
}
