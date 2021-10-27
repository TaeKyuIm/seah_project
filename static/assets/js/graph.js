// get value
var C_value;
var Cr_value;
var Mo_value;
var Mn_value;
var Si_value;
var P_value;
var S_value;
var Ni_value;
var Cu_value;
var Sn_value;
var Al_value;
var V_value;
var Ti_value;
var B_value;
var N_value;
var Nb_value;
var Ca_value;
var D_value;
var etc;

function getValueInput() {
  document.getElementsByID("bt").oncilck = function () {
    document.getElementsById("chemical").submit();
  };
  C_value = document.getElementByID("C_value").value;
  Cr_value = document.getElementByID("Cr_value").value;
  Mo_value = document.getElementByID("Mo_value").value;
  Mn_value = document.getElementByID("Mn_value").value;
  Si_value = document.getElementByID("Si_value").value;
  P_value = document.getElementByID("P_value").value;
  S_value = document.getElementByID("S_value").value;
  Ni_value = document.getElementByID("Ni_value").value;
  Cu_value = document.getElementByID("Cu_value").value;
  Sn_value = document.getElementByID("Sn_value").value;
  Al_value = document.getElementByID("Al_value").value;
  V_value = document.getElementByID("V_value").value;
  Ti_value = document.getElementByID("Ti_value").value;
  B_value = document.getElementByID("B_value").value;
  N_value = document.getElementByID("N_value").value;
  Nb_value = document.getElementByID("Nb_value").value;
  Ca_value = document.getElementByID("Ca_value").value;
  D_value = document.getElementByID("D_value").value;
  etc =
    Si_value +
    P_value +
    S_value +
    Ni_value +
    Cu_value +
    Sn_value +
    Al_value +
    Al_value +
    V_value +
    Ti_value +
    Ti_value +
    B_value +
    N_value +
    Nb_value +
    Ca_value;
}

//pie chart
google.charts.load("current", { packages: ["corechart"] });
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
  var data = new google.visualization.arrayToDataTable([
    ["Element", "weight percent (wt%)"],
    ["C", C_value],
    ["Mn", Mn_value],
    ["Cr", Cr_value],
    ["Mo", Mo_value],
    ["etc.", etc],
  ]);

  var options = {
    title: "원소함량분포",
    width: 520,
    height: 380,
  };

  var chart = new google.visualization.PieChart(
    document.getElementById("piechart")
  );

  chart.draw(data, options);
}

// text table
google.charts.load("current", { packages: ["table"] });
google.charts.setOnLoadCallback(drawTable);

function drawTable() {
  var data = new google.visualization.DataTable();
  data.addColumn("string", "거리");
  data.addColumn("number", "경도");
  data.addColumn("boolean", "탄소함량 0.25 이상");
  data.addRows([
    ["1.5", { v: 46.766667, f: "46.766667" }, true],
    ["3", { v: 45.76667, f: "45.76667" }, false],
    ["5", { v: 43.4, f: "43.4" }, true],
    ["7", { v: 38.2667, f: "38.2667" }, true],
    ["9", { v: 33.6, f: "33.6" }, false],
    ["11", { v: 30.1, f: "30.1" }, false],
    ["13", { v: 28.2, f: "28.2" }, false],
  ]);

  var options = { width: 520, height: 380 };

  var table = new google.visualization.Table(
    document.getElementById("table_div")
  );

  table.draw(data, {
    showRowNumber: true,
    width: "100%",
    height: "100%",
  });
}

//line chart
google.charts.load("current", { packages: ["corechart"] });
google.charts.setOnLoadCallback(drawChartL);
function drawChartL() {
  var data = new google.visualization.DataTable();
  data.addColumn("number", "x");
  data.addColumn("number", "values");
  data.addColumn({ id: "i0", type: "number", role: "interval" });
  data.addColumn({ id: "i1", type: "number", role: "interval" });
  data.addColumn({ id: "i2", type: "number", role: "interval" });
  data.addColumn({ id: "i2", type: "number", role: "interval" });
  data.addColumn({ id: "i2", type: "number", role: "interval" });

  data.addRows([
    [1.5, 100, 90, 110, 85, 96, 104],
    [2, 120, 95, 130, 90, 113, 124],
    [3, 130, 105, 140, 100, 117, 133],
    [4, 90, 85, 95, 85, 88, 92],
    [5, 70, 74, 63, 67, 69, 70],
    [6, 30, 39, 22, 21, 28, 34],
    [7, 80, 77, 83, 70, 77, 85],
    [8, 100, 90, 110, 85, 95, 102],
  ]);

  // The intervals data as narrow lines (useful for showing raw source data)
  var options_lines = {
    title: "Line intervals, default",
    curveType: "function",
    lineWidth: 4,
    intervals: { style: "line" },
    legend: "none",
    width: 1100,
    height: 500,
  };

  var chart_lines = new google.visualization.LineChart(
    document.getElementById("chart_lines")
  );
  chart_lines.draw(data, options_lines);
}
