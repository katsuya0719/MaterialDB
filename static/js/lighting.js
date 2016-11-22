var data = "x,y,z\n" +
    "1,1,3\n" +
    "5,2,11\n" +
    "13,13,13\n"+
    "5,3,20\n"+
    "12,12,10\n"+
    "3,6,8\n"+
    "15,2,9\n"+
    "8,6,14\n"+
    "1,4,9\n"+
    "8,8,12\n";

function readapi(data){
    console.log(data);
    var data = d3.csv.parse(data);
    data.forEach(function (x) {
        x.x = +x.x;
        x.y = +x.y;
        x.z = +x.z;
    });
    var ndx = crossfilter(data),
        dim1 = ndx.dimension(function (d) {
            return [+d.x, +d.y];
        }),
        dim2 = ndx.dimension(function (d) {
            return [+d.y, +d.z];
        }),
        group1 = dim1.group(),
        group2 = dim2.group();
    chart1.width(300)
        .height(300)
        .x(d3.scale.linear().domain([0, 20]))
        .yAxisLabel("y")
        .xAxisLabel("x")
        .clipPadding(10)
        .dimension(dim1)
        .excludedOpacity(0.5)
        .group(group1);
    chart2.width(300)
        .height(300)
        .x(d3.scale.linear().domain([0, 20]))
        .yAxisLabel("z")
        .xAxisLabel("y")
        .clipPadding(10)
        .dimension(dim2)
        .excludedColor('#ddd')
        .group(group2);
    dc.renderAll();
};

readapi(data);