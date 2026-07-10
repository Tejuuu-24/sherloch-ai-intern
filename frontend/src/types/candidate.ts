/**
 * Domain types for the AI Interview Candidate Identification System.
 * These mirror the FastAPI `/identify` response contract exactly.
 */

export interface Candidate {
  display_name: string;
  email: string;
}

/** A single participant detected in the session, ranked by relevance score. */
export interface Participant {
  display_name: string;
  email: string;
  score: number;
}

/**
 * Raw shape returned by `GET /identify`.
 * Evidence and participants are optional/nullable in practice, so the
 * client treats them defensively rather than assuming they are populated.
 */
export interface IdentifyResponse {
  candidate: Candidate | null;
  confidence: number;
  is_candidate: boolean;
  summary: string;
  reason: string;
  evidence: string[] | null;
  participants: Participant[] | null;
}
