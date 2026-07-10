const TECH_STACK = [
  "FastAPI",
  "YOLOv8",
  "Whisper",
  "Gemini",
  "React",
  "Tailwind CSS",
] as const;

export function Footer() {
  return (
    <footer className="border-t border-border bg-surface">
      <div className="mx-auto flex max-w-6xl flex-col items-center gap-4 px-6 py-10 text-center">
        <p className="text-xs font-semibold uppercase tracking-wider text-ink-muted">
          Built on
        </p>
        <div className="flex flex-wrap items-center justify-center gap-2">
          {TECH_STACK.map((tech) => (
            <span
              key={tech}
              className="rounded-full border border-border bg-white px-3.5 py-1.5 text-xs font-medium text-ink-soft shadow-[var(--shadow-card)]"
            >
              {tech}
            </span>
          ))}
        </div>
        <p className="text-xs text-ink-muted">
          © {new Date().getFullYear()} Sherlock AI. Candidate identification
          powered by multimodal reasoning.
        </p>
      </div>
    </footer>
  );
}
