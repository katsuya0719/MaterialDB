function plotly(){
    var endpoint = '/hvac/api/chart/data'
    var copData = capacityData = []
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function(data){
            capacityData = data.capacity.map(function(ele){
                return ele/1000;
            });
            copData = data.cop;
            console.log(copData);
            scatterChart()
            //transcriptChart()
        // console.log(data)
        },
        error: function(error_data){
            console.log("error")
            console.log(error_data)
        },
    })

    function scatterChart(){
        var data = [{
            x: capacityData,
            y: copData,
            type: 'scatter',
            name: 'chiller',
            mode: 'markers',
            marker: { size: 8 }
        }];
        var layout = {
            title: 'Relationship between capacity and COP',
            titlefont: {
                family: 'Droid Sans Mono',
                size: 36,
                color: '#000000'
            },
            xaxis: {
                title: 'Cooling Capacity[kW]',
                titlefont: {
                  size: 18,
                  color: '#7f7f7f'
                }
              },
              yaxis: {
                title: 'COP []',
                titlefont: {
                  size: 18,
                  color: '#7f7f7f'
                }
              }
            //margin: {l:200},
        };

        Plotly.newPlot('scatter', data, layout);
    }

    function articleChart(){
        var data = [{
            x: articleData,
            y: articleLabels,
            type: 'bar',
            orientation: 'h',
            marker: {
                color: '#23b7e5',
            },
        }];
        var layout = {
            title: 'Number of Articles per Company',
            titlefont: {
                family: 'Droid Sans Mono',
                size: 36,
                color: '#000000'
            },
            margin: {l:200},
        };

        Plotly.newPlot('articles', data, layout);
    }
}
