function plotly(){
    var endpoint = '/hvac/api/chart/data'
    var copData = capacityData = idData = []
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function(data){
            capacityData = data.capacity.map(function(ele){
                return ele/1000;
            });
            copData = data.cop;
            idData = data.id;
            //console.log(idData);
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
        d3=Plotly.d3;
        var data = [{
            x: capacityData,
            y: copData,
            type: 'scatter',
            name: idData,
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

        var plot=document.getElementById('scatter');
        var hoverInfo=document.getElementById('hoverInfo');

        //add callback
        /*
        plot.on('plotly_click', function(data){
            var pts = '';
            for(var i=0; i < data.points.length; i++){

                pts = 'x = '+data.points[i].x +'\ny = '+
                    data.points[i].y.toPrecision(4) + '\nid='+idData[i]+'\n\n';
            }
            alert('Closest point clicked:\n\n'+pts);
        });
        */
        plot.on('plotly_hover', function(data){
            var infotext = data.points.map(function(d){
                console.log(d);
              return (d.data.name[d.pointIndex]+'/Capacity= '+d.x+'kW, COP= '+d.y.toPrecision(3));
            });
            console.log(infotext)
            hoverInfo.innerHTML = infotext.join('');
        })
         .on('plotly_unhover', function(data){
            hoverInfo.innerHTML = '';
        });
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
