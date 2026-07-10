import axios from "axios";

/**
 * Base URL for the FastAPI backend.
 * Configure via `VITE_API_BASE_URL` in a `.env` file; falls back to the
 * conventional local FastAPI dev port.
 */
export const API_BASE_URL: string =
  import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000";

export const httpClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 300_000,
  headers: {
    Accept: "application/json",
  },
});
