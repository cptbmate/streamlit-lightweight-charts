# streamlit-lightweight-charts
Streamlit wrapper for performant Tradingview's Financial: `lightweight-charts`

The Lightweight Charts library is the best choice to display financial data as an interactive chart on a web page without affecting loading speed and performance.

- [Features Demo](https://www.tradingview.com/lightweight-charts/)
- [Documentation](https://tradingview.github.io/lightweight-charts/)
- [GitHub](https://github.com/tradingview/lightweight-charts)

## How to use:
```
renderLightweightCharts(charts: <List of Dicts> , key: <str>)
```

### API
- charts: `<List of Dicts>`

    - [chart](https://tradingview.github.io/lightweight-charts/docs/api/interfaces/ChartOptions): `<Dict>`

    - [series](https://tradingview.github.io/lightweight-charts/docs/series-types): `<List of Dicts>`

        - [type](https://tradingview.github.io/lightweight-charts/docs/series-types): `<str-enum>`
            [ Area, Bar, Baseline, Candlestick, Histogram, Line ]

        - data: `<List of Dicts>` accordingly to series type

        - options: `<Dict>` with style options

        - priceScale: `<Dict>` optional

- key: `<str>` when creating multiple charts in one page

<br/>

# e.g.:
<br />

# Overlaid Charts

![Price with Volume Chart](https://github.com/freyastreamlit/streamlit-lightweight-charts/blob/main/examples/PriceVolumeChart.png?raw=true)

```python
import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts
import streamlit_lightweight_charts.dataSamples as data

priceVolumeChartOptions = {
    "height": 400,
    "rightPriceScale": {
        "scaleMargins": {
            "top": 0.2,
            "bottom": 0.25,
        },
        "borderVisible": False,
    },
    "overlayPriceScales": {
        "scaleMargins": {
            "top": 0.7,
            "bottom": 0,
        }
    },
    "layout": {
        "background": {
            "type": 'solid',
            "color": '#131722'
        },
        "textColor": '#d1d4dc',
    },
    "grid": {
        "vertLines": {
            "color": 'rgba(42, 46, 57, 0)',
        },
        "horzLines": {
            "color": 'rgba(42, 46, 57, 0.6)',
        }
    }
}

priceVolumeSeries = [
    {
        "type": 'Area',
        "data": data.priceVolumeSeriesArea,
        "options": {
            "topColor": 'rgba(38,198,218, 0.56)',
            "bottomColor": 'rgba(38,198,218, 0.04)',
            "lineColor": 'rgba(38,198,218, 1)',
            "lineWidth": 2,
        }
    },
    {
        "type": 'Histogram',
        "data": data.priceVolumeSeriesHistogram,
        "options": {
            "color": '#26a69a',
            "priceFormat": {
                "type": 'volume',
            },
            "priceScaleId": "" # set as an overlay setting,
        },
        "priceScale": {
            "scaleMargins": {
                "top": 0.7,
                "bottom": 0,
            }
        }
    }
]
st.subheader("Price and Volume Series Chart sample")

renderLightweightCharts([
    {
        "chart": priceVolumeChartOptions,
        "series": priceVolumeSeries
    }
], 'priceAndVolume')
```
---
<br />

![Overlaid Areas Chart](https://github.com/freyastreamlit/streamlit-lightweight-charts/blob/main/examples/OverlaidAreasChart.png?raw=true)

```python
import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts
import streamlit_lightweight_charts.dataSamples as data

overlaidAreaSeriesOptions = {
    "height": 400,
    "rightPriceScale": {
        "scaleMargins": {
            "top": 0.1,
            "bottom": 0.1,
        },
        "mode": 2, # PriceScaleMode: 0-Normal, 1-Logarithmic, 2-Percentage, 3-IndexedTo100
        "borderColor": 'rgba(197, 203, 206, 0.4)',
    },
    "timeScale": {
        "borderColor": 'rgba(197, 203, 206, 0.4)',
    },
    "layout": {
        "background": {
            "type": 'solid',
            "color": '#100841'
        },
        "textColor": '#ffffff',
    },
    "grid": {
        "vertLines": {
            "color": 'rgba(197, 203, 206, 0.4)',
            "style": 1, # LineStyle: 0-Solid, 1-Dotted, 2-Dashed, 3-LargeDashed
        },
        "horzLines": {
            "color": 'rgba(197, 203, 206, 0.4)',
            "style": 1, # LineStyle: 0-Solid, 1-Dotted, 2-Dashed, 3-LargeDashed
        }
    }
}

seriesOverlaidChart = [
    {
        "type": 'Area',
        "data": data.seriesMultipleChartArea01,
        "options": {
            "topColor": 'rgba(255, 192, 0, 0.7)',
            "bottomColor": 'rgba(255, 192, 0, 0.3)',
            "lineColor": 'rgba(255, 192, 0, 1)',
            "lineWidth": 2,
        }
    },
    {
        "type": 'Area',
        "data": data.seriesMultipleChartArea02,
        "options": {
            "topColor": 'rgba(67, 83, 254, 0.7)',
            "bottomColor": 'rgba(67, 83, 254, 0.3)',
            "lineColor": 'rgba(67, 83, 254, 1)',
            "lineWidth": 2,
        }
    }
]
st.subheader("Overlaid Series Chart sample")

renderLightweightCharts([
    {
        "chart": overlaidAreaSeriesOptions,
        "series": seriesOverlaidChart
    }
], 'overlaid')
```
---
<br />

# Multi Pane charts

![Multi Pane Charts](https://github.com/freyastreamlit/streamlit-lightweight-charts/blob/main/examples/MultiPaneChart.png?raw=true)

```python
import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts
import streamlit_lightweight_charts.dataSamples as data

chartMultipaneOptions = [
    {
        "width": 600,
        "height": 400,
        "layout": {
            "background": {
                "type": "solid",
                "color": 'white'
            },
            "textColor": "black"
        },
        "grid": {
            "vertLines": {
                "color": "rgba(197, 203, 206, 0.5)"
                },
            "horzLines": {
                "color": "rgba(197, 203, 206, 0.5)"
            }
        },
        # "crosshair": {
        #     "mode": 0
        # },
        "priceScale": {
            "borderColor": "rgba(197, 203, 206, 0.8)"
        },
        "timeScale": {
            "borderColor": "rgba(197, 203, 206, 0.8)",
            "barSpacing": 15
            # "fixLeftEdge": True,
        }
    },
    {
        "width": 600,
        "height": 100,
        "rightPriceScale": {
            "scaleMargins": {
                "top": 0.2,
                "bottom": 0.25,
            },
            # "borderVisible": False,
        },
        "overlayPriceScales": {
            "scaleMargins": {
                "top": 0.7,
                "bottom": 0,
            }
        },
        "crosshair": {
            "mode": 0
        },
        "layout": {
            "background": {
                "type": 'solid',
                "color": 'white'
            },
            "textColor": 'black',
        },
        "grid": {
            "vertLines": {
                "color": 'rgba(42, 46, 57, 0)',
            },
            "horzLines": {
                "color": 'rgba(42, 46, 57, 0.6)',
            }
        },
        "timeScale": {
            "visible": False,
        }
    },
    {
        "width": 600,
        "height": 200,
        "layout": {
            "background": {
                "type": "solid",
                "color": 'white'
            },
            "textColor": "black"
        },
        "timeScale": {
            "visible": False,
        }
    }
]

seriesCandlestickChart = [
    {
        "type": 'Candlestick',
        "data": data.priceCandlestickMultipane,
        "options": {
            "upColor": '#26a69a',
            "downColor": '#ef5350',
            "borderVisible": False,
            "wickUpColor": '#26a69a',
            "wickDownColor": '#ef5350'
        }
    }
]

seriesAreaChart = [
    {
        "type": 'Baseline',
        "data": data.priceBaselineMultipane,
        "options": {
            "baseValue": { "type": "price", "price": 180 },
            "topLineColor": 'rgba( 38, 166, 154, 1)',
            "topFillColor1": 'rgba( 38, 166, 154, 0.28)',
            "topFillColor2": 'rgba( 38, 166, 154, 0.05)',
            "bottomLineColor": 'rgba( 239, 83, 80, 1)',
            "bottomFillColor1": 'rgba( 239, 83, 80, 0.05)',
            "bottomFillColor2": 'rgba( 239, 83, 80, 0.28)'
        }
    }
]

seriesHistogramChart = [
    {
        "type": 'Histogram',
        "data": data.priceVolumeMultipane,
        "options": {
            "color": '#26a69a',
            "priceFormat": {
                "type": 'volume',
            },
            "priceScaleId": "" # set as an overlay setting,
        },
        "priceScale": {
            "scaleMargins": {
                "top": 0,
                "bottom": 0,
            },
            "alignLabels": False
        }
    }
]

st.subheader("Multipane Chart sample")
renderLightweightCharts([
    {
        "chart": chartMultipaneOptions[0],
        "series": seriesCandlestickChart
    },
    {
        "chart": chartMultipaneOptions[1],
        "series": seriesHistogramChart
    },
            {
        "chart": chartMultipaneOptions[2],
        "series": seriesAreaChart
    }
], 'multipane')

```
---
<br />

# Basic charts

![Line Chart](https://github.com/freyastreamlit/streamlit-lightweight-charts/blob/main/examples/LineChart.png?raw=true)

```python
import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts

chartOptions = {
    "layout": {
        "textColor": 'black',
        "background": {
            "type": 'solid',
            "color": 'white'
        }
    }
}

seriesLineChart = [{
    "type": 'Line',
    "data": [
        { "time": '2018-12-22', "value": 32.51 },
        { "time": '2018-12-23', "value": 31.11 },
        { "time": '2018-12-24', "value": 27.02 },
        { "time": '2018-12-25', "value": 27.32 },
        { "time": '2018-12-26', "value": 25.17 },
        { "time": '2018-12-27', "value": 28.89 },
        { "time": '2018-12-28', "value": 25.46 },
        { "time": '2018-12-29', "value": 23.92 },
        { "time": '2018-12-30', "value": 22.68 },
        { "time": '2018-12-31', "value": 22.67 },
    ],
    "options": {}
}]

st.subheader("Line Chart sample")

renderLightweightCharts([
    {
        "chart": chartOptions,
        "series": seriesLineChart
    }
], 'line')
```
---
<br />

![Area Chart](https://github.com/freyastreamlit/streamlit-lightweight-charts/blob/main/examples/AreaChart.png?raw=true)

```python
import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts

chartOptions = {
    "layout": {
        "textColor": 'black',
        "background": {
            "type": 'solid',
            "color": 'white'
        }
    }
}

seriesAreaChart = [{
    "type": 'Area',
    "data": [
        { "time": '2018-12-22', "value": 32.51 },
        { "time": '2018-12-23', "value": 31.11 },
        { "time": '2018-12-24', "value": 27.02 },
        { "time": '2018-12-25', "value": 27.32 },
        { "time": '2018-12-26', "value": 25.17 },
        { "time": '2018-12-27', "value": 28.89 },
        { "time": '2018-12-28', "value": 25.46 },
        { "time": '2018-12-29', "value": 23.92 },
        { "time": '2018-12-30', "value": 22.68 },
        { "time": '2018-12-31', "value": 22.67 },
    ],
    "options": {}
}]

st.subheader("Area Chart sample")
renderLightweightCharts( [
    {
        "chart": chartOptions,
        "series": seriesAreaChart,
    }
], 'area')
```
---
<br />

![Histogram Chart](https://github.com/freyastreamlit/streamlit-lightweight-charts/blob/main/examples/HistogramChart.png?raw=true)

```python
import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts

chartOptions = {
    "layout": {
        "textColor": 'black',
        "background": {
            "type": 'solid',
            "color": 'white'
        }
    }
}

seriesHistogramChart = [{
    "type": 'Histogram',
    "data": [
        { "value": 1, "time": 1642425322 },
        { "value": 8, "time": 1642511722 },
        { "value": 10, "time": 1642598122 },
        { "value": 20, "time": 1642684522 },
        { "value": 3, "time": 1642770922, "color": 'red' },
        { "value": 43, "time": 1642857322 },
        { "value": 41, "time": 1642943722, "color": 'red' },
        { "value": 43, "time": 1643030122 },
        { "value": 56, "time": 1643116522 },
        { "value": 46, "time": 1643202922, "color": 'red' }
    ],
    "options": { "color": '#26a69a' }
}]

st.subheader("Histogram Chart sample")

renderLightweightCharts([
    {
        "chart": chartOptions,
        "series": seriesHistogramChart
    }
], 'histogram')
```
---
<br />

![Bar Chart](https://github.com/freyastreamlit/streamlit-lightweight-charts/blob/main/examples/BarChart.png?raw=true)

```python
import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts

chartOptions = {
    "layout": {
        "textColor": 'black',
        "background": {
            "type": 'solid',
            "color": 'white'
        }
    }
}

seriesBarChart = [{
    "type": 'Bar',
    "data": [
        { "open": 10, "high": 10.63, "low": 9.49, "close": 9.55, "time": 1642427876 },
        { "open": 9.55, "high": 10.30, "low": 9.42, "close": 9.94, "time": 1642514276 },
        { "open": 9.94, "high": 10.17, "low": 9.92, "close": 9.78, "time": 1642600676 },
        { "open": 9.78, "high": 10.59, "low": 9.18, "close": 9.51, "time": 1642687076 },
        { "open": 9.51, "high": 10.46, "low": 9.10, "close": 10.17, "time": 1642773476 },
        { "open": 10.17, "high": 10.96, "low": 10.16, "close": 10.47, "time": 1642859876 },
        { "open": 10.47, "high": 11.39, "low": 10.40, "close": 10.81, "time": 1642946276 },
        { "open": 10.81, "high": 11.60, "low": 10.30, "close": 10.75, "time": 1643032676 },
        { "open": 10.75, "high": 11.60, "low": 10.49, "close": 10.93, "time": 1643119076 },
        { "open": 10.93, "high": 11.53, "low": 10.76, "close": 10.96, "time": 1643205476 }
    ],
    "options": {
        "upColor": '#26a69a',
        "downColor": '#ef5350'
    }
}]

st.subheader("Bar Chart sample")
renderLightweightCharts([
    {
        "chart": chartOptions,
        "series": seriesBarChart
    }
], 'bar')
```
---
<br />

![Candlestick Chart](https://github.com/freyastreamlit/streamlit-lightweight-charts/blob/main/examples/CandlestickChart.png?raw=true)

```python
import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts

chartOptions = {
    "layout": {
        "textColor": 'black',
        "background": {
            "type": 'solid',
            "color": 'white'
        }
    }
}

seriesCandlestickChart = [{
    "type": 'Candlestick',
    "data": [
        { "open": 10, "high": 10.63, "low": 9.49, "close": 9.55, "time": 1642427876 },
        { "open": 9.55, "high": 10.30, "low": 9.42, "close": 9.94, "time": 1642514276 },
        { "open": 9.94, "high": 10.17, "low": 9.92, "close": 9.78, "time": 1642600676 },
        { "open": 9.78, "high": 10.59, "low": 9.18, "close": 9.51, "time": 1642687076 },
        { "open": 9.51, "high": 10.46, "low": 9.10, "close": 10.17, "time": 1642773476 },
        { "open": 10.17, "high": 10.96, "low": 10.16, "close": 10.47, "time": 1642859876 },
        { "open": 10.47, "high": 11.39, "low": 10.40, "close": 10.81, "time": 1642946276 },
        { "open": 10.81, "high": 11.60, "low": 10.30, "close": 10.75, "time": 1643032676 },
        { "open": 10.75, "high": 11.60, "low": 10.49, "close": 10.93, "time": 1643119076 },
        { "open": 10.93, "high": 11.53, "low": 10.76, "close": 10.96, "time": 1643205476 }
    ],
    "options": {
        "upColor": '#26a69a',
        "downColor": '#ef5350',
        "borderVisible": False,
        "wickUpColor": '#26a69a',
        "wickDownColor": '#ef5350'
    }
}]

st.subheader("Candlestick Chart sample")

renderLightweightCharts([
    {
        "chart": chartOptions,
        "series": seriesCandlestickChart
    }
], 'candlestick')
```
---
<br />

![Baseline Chart](https://github.com/freyastreamlit/streamlit-lightweight-charts/blob/main/examples/BaselineChart.png?raw=true)

```python
import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts

chartOptions = {
    "layout": {
        "textColor": 'black',
        "background": {
            "type": 'solid',
            "color": 'white'
        }
    }
}

seriesBaselineChart = [{
    "type": 'Baseline',
    "data": [
        { "value": 1, "time": 1642425322 },
        { "value": 8, "time": 1642511722 },
        { "value": 10, "time": 1642598122 },
        { "value": 20, "time": 1642684522 },
        { "value": 3, "time": 1642770922 },
        { "value": 43, "time": 1642857322 },
        { "value": 41, "time": 1642943722 },
        { "value": 43, "time": 1643030122 },
        { "value": 56, "time": 1643116522 },
        { "value": 46, "time": 1643202922 }
    ],
    "options": {
        "baseValue": { "type": "price", "price": 25 },
        "topLineColor": 'rgba( 38, 166, 154, 1)',
        "topFillColor1": 'rgba( 38, 166, 154, 0.28)',
        "topFillColor2": 'rgba( 38, 166, 154, 0.05)',
        "bottomLineColor": 'rgba( 239, 83, 80, 1)',
        "bottomFillColor1": 'rgba( 239, 83, 80, 0.05)',
        "bottomFillColor2": 'rgba( 239, 83, 80, 0.28)'
    }
}]

st.subheader("Baseline Chart sample")

renderLightweightCharts([
    {
        "chart": chartOptions,
        "series": seriesBaselineChart
    }
], 'baseline')
```
