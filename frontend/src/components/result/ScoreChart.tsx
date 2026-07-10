import {
  Bar,
  BarChart,
  CartesianGrid,
  Cell,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { EmptyState } from "@/components/common/EmptyState";
import type { Participant } from "@/types/candidate";

interface ScoreChartProps {
  participants: Participant[];
}

const INDIGO = "#4a41e0";
const INDIGO_MUTED = "#c7c4f7";

export function ScoreChart({ participants }: ScoreChartProps) {
  const sorted = [...participants].sort((a, b) => b.score - a.score);
  const topScore = sorted[0]?.score;

  if (sorted.length === 0) {
    return (
      <Card>
        <CardHeader>
          <CardTitle>Score Distribution</CardTitle>
        </CardHeader>
        <CardContent>
          <EmptyState
            title="No scores to chart"
            description="Participant scores will appear here once the backend returns data."
          />
        </CardContent>
      </Card>
    );
  }

  const chartHeight = Math.max(sorted.length * 56, 160);

  return (
    <Card>
      <CardHeader>
        <CardTitle>Score Distribution</CardTitle>
        <CardDescription>Relative identification confidence per participant</CardDescription>
      </CardHeader>
      <CardContent>
        <div style={{ width: "100%", height: chartHeight }}>
          <ResponsiveContainer>
            <BarChart
              data={sorted}
              layout="vertical"
              margin={{ top: 4, right: 24, bottom: 4, left: 4 }}
              barCategoryGap={16}
            >
              <CartesianGrid horizontal={false} stroke="#e6e7eb" />
              <XAxis
                type="number"
                domain={[0, 100]}
                tick={{ fill: "#8b8ea1", fontSize: 12 }}
                axisLine={{ stroke: "#e6e7eb" }}
                tickLine={false}
              />
              <YAxis
                type="category"
                dataKey="display_name"
                width={110}
                tick={{ fill: "#101223", fontSize: 13, fontWeight: 500 }}
                axisLine={{ stroke: "#e6e7eb" }}
                tickLine={false}
              />
              <Tooltip
                cursor={{ fill: "#f7f8fa" }}
                contentStyle={{
                  borderRadius: 12,
                  border: "1px solid #e6e7eb",
                  fontSize: 13,
                }}
              />
              <Bar dataKey="score" radius={[0, 8, 8, 0]} maxBarSize={28}>
                {sorted.map((entry, index) => (
                  <Cell
                    key={entry.email ?? index}
                    fill={entry.score === topScore ? INDIGO : INDIGO_MUTED}
                  />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>
      </CardContent>
    </Card>
  );
}
