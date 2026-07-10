import { ShieldCheck, Wifi, WifiOff } from "lucide-react";
import { Badge } from "@/components/ui/badge";

interface NavbarProps {
  isBackendConnected: boolean;
}

export function Navbar({ isBackendConnected }: NavbarProps) {
  return (
    <header className="sticky top-0 z-40 border-b border-border bg-white/80 backdrop-blur-md">
      <div className="mx-auto flex h-16 max-w-6xl items-center justify-between px-6">
        <div className="flex items-center gap-3">
          <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-indigo-600 shadow-sm">
            <ShieldCheck className="h-5 w-5 text-white" strokeWidth={2.25} />
          </div>
          <div className="flex flex-col leading-tight">
            <span className="font-display text-[15px] font-bold tracking-tight text-ink">
              Sherlock AI
            </span>
            <span className="text-xs font-medium text-ink-muted">
              Interview Candidate Identification
            </span>
          </div>
        </div>

        <Badge tone={isBackendConnected ? "success" : "danger"}>
          {isBackendConnected ? (
            <Wifi className="h-3.5 w-3.5" />
          ) : (
            <WifiOff className="h-3.5 w-3.5" />
          )}
          {isBackendConnected ? "Backend Connected" : "Backend Unreachable"}
        </Badge>
      </div>
    </header>
  );
}
