import { Navbar } from "@/components/layout/Navbar";
import { Footer } from "@/components/layout/Footer";
import { Hero } from "@/components/hero/Hero";
import { ResultSummary } from "@/components/result/ResultSummary";
import { ReasoningCard } from "@/components/result/ReasoningCard";
import { EvidenceTimeline } from "@/components/result/EvidenceTimeline";
import { ParticipantsTable } from "@/components/result/ParticipantsTable";
import { ScoreChart } from "@/components/result/ScoreChart";
import { ArchitectureDiagram } from "@/components/architecture/ArchitectureDiagram";
import { ErrorState } from "@/components/common/ErrorState";
import { EmptyState } from "@/components/common/EmptyState";
import { useIdentifyCandidate } from "@/hooks/useIdentifyCandidate";

function App() {
  const { status, data, errorMessage, runAnalysis } = useIdentifyCandidate();

  const hasResult = status === "success" && data !== null;
  const isBackendConnected = status !== "error";

  return (
    <div className="flex min-h-screen flex-col bg-canvas">
      <Navbar isBackendConnected={isBackendConnected} />

      <main className="flex-1">
        <Hero isLoading={status === "loading"} onAnalyze={runAnalysis} />

        <section className="mx-auto flex max-w-6xl flex-col gap-6 px-6 py-14">
          {status === "idle" && (
            <EmptyState
              title="No analysis run yet"
              description='Click "Analyze Candidate" above to run identification against your FastAPI backend.'
            />
          )}

          {status === "error" && errorMessage && (
            <ErrorState message={errorMessage} onRetry={runAnalysis} />
          )}

          {hasResult && (
            <>
              <ResultSummary
                candidate={data.candidate}
                confidence={data.confidence}
                isCandidate={data.is_candidate}
              />

              <ReasoningCard summary={data.summary} reason={data.reason} />

              <div className="grid gap-6 lg:grid-cols-2">
                <EvidenceTimeline evidence={data.evidence ?? []} />
                <ScoreChart participants={data.participants ?? []} />
              </div>

              <ParticipantsTable participants={data.participants ?? []} />
            </>
          )}
        </section>

        <section className="mx-auto max-w-6xl px-6 pb-16">
          <ArchitectureDiagram />
        </section>
      </main>

      <Footer />
    </div>
  );
}

export default App;
