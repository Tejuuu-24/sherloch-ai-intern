# Sherlock AI — Interview Candidate Identification Dashboard

An enterprise-grade React dashboard for an AI Interview Candidate
Identification System. It calls a single FastAPI endpoint
(`GET /identify`) and visualizes the result: candidate identity,
confidence score, AI reasoning, evidence timeline, participant
ranking, and score distribution.

## Tech stack

- React 19 + Vite + TypeScript
- Tailwind CSS v4
- shadcn/ui-style primitives (Button, Card, Badge) built with
  `class-variance-authority` + `tailwind-merge`
- Axios (service layer)
- Lucide React (icons)
- Recharts (score bar chart)

## Getting started

```bash
npm install
cp .env.example .env.local   # point this at your FastAPI backend
npm run dev
```

The app runs at `http://localhost:5173` by default.

### Environment variables

| Variable            | Description                    | Default                 |
| ------------------- | ------------------------------- | ------------------------ |
| `VITE_API_BASE_URL`  | Base URL of the FastAPI backend | `http://localhost:8000` |

The backend must expose `GET /identify` and, since this app calls it
directly from the browser, must send CORS headers allowing the
dashboard's origin (e.g. `Access-Control-Allow-Origin: *` in
development).

## Scripts

- `npm run dev` — start the Vite dev server
- `npm run build` — type-check (`tsc -b`) and produce a production build in `dist/`
- `npm run preview` — preview the production build locally
- `npm run lint` — run oxlint

## Project structure

```
src/
  components/
    ui/            Reusable primitives: Button, Card, Badge
    layout/        Navbar, Footer
    hero/          Hero section with the "Analyze Candidate" CTA
    result/        ResultSummary, ConfidenceCircle, ReasoningCard,
                   EvidenceTimeline, ParticipantsTable, ScoreChart
    architecture/  ArchitectureDiagram (pipeline visualization)
    common/        Spinner, ErrorState, EmptyState
  hooks/
    useIdentifyCandidate.ts   Loading/error/data state machine for GET /identify
  services/
    httpClient.ts             Axios instance (base URL, timeout)
    candidateService.ts       identifyCandidate() + typed error handling
  types/
    candidate.ts               TypeScript interfaces matching the API contract
  App.tsx
  main.tsx
  index.css                   Tailwind v4 theme tokens (colors, fonts)
```

## API contract

```http
GET /identify
```

```json
{
  "candidate": { "display_name": "Tejaswini Sanam", "email": "tejaswini@gmail.com" },
  "confidence": 95,
  "is_candidate": true,
  "summary": "...",
  "reason": "...",
  "evidence": ["..."],
  "participants": [{ "display_name": "...", "email": "...", "score": 0 }]
}
```

`candidate`, `evidence`, and `participants` are treated as nullable on
the client, so the UI degrades gracefully (empty states) if the
backend omits them.

## Design notes

- **Palette**: white canvas, light-gray surfaces, indigo accent,
  green for a positive identification, red for a negative one.
- **Typography**: Manrope for display/headings, Inter for UI text,
  JetBrains Mono for scores and code-like values.
- **States handled**: idle (before first analysis), loading (spinner
  in the CTA), success (full result), error (retryable error banner),
  and empty (graceful fallback if evidence/participants are missing).
