// TODO make this a string enum in TypeScript 2.4

export type ChartTypeType = "LineChart" | "ScatterPlot" | "StackedArea" | "DiscreteBar" | "SlopeChart"

export default class ChartType {
    static LineChart = "LineChart"
    static ScatterPlot = "ScatterPlot"
    static StackedArea = "StackedArea"
    static DiscreteBar = "DiscreteBar"
    static SlopeChart = "SlopeChart"
}
