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
            scatterChart()
            //test()
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
        plot.on('plotly_hover', function(data){
            var infotext = data.points.map(function(d){
              return (d.data.name[d.pointIndex]+'/Capacity= '+d.x+'kW, COP= '+d.y.toPrecision(3));
            });
            hoverInfo.innerHTML = infotext.join('');
        })
         .on('plotly_unhover', function(data){
            hoverInfo.innerHTML = '';
        });
        plot.on('plotly_click', function(data){
            var url = data.points.map(function(d){
                return '/hvac/api/'+d.data.name[d.pointIndex]
            })
            scatter3d(url)
        });
    }
}

function scatter3d(url){
    console.log("3d")
    $.ajax({
        method: "GET",
        url: url,
        success: function(data){
            console.log(data);
            //capacity function
            var cap=biquadratic(data.cap,data.capacity)
            //var eirplr=biquadratic(data.eirplr)
            render(cap,'cap','Cooling Capacity Function')
            //copData = data.cop;
        },
        error: function(error_data){
            console.log("error")
            console.log(error_data)
        },
    })

    function biquadratic(d,coef){
        console.log(d)
        var X=_.range(Math.floor(d.min_x), Math.ceil(d.max_x), 1);
        var Y=_.range(Math.floor(d.min_y), Math.ceil(d.max_y), 1);
        var xList=[];
        var yList=[];
        var zList=[];

        X.forEach(function(x){
            Y.forEach(function(y){
                console.log(x,y)
                xList.push(x)
                yList.push(y)
                var z=d.c1+d.c2*x+d.c3*Math.pow(x,2)+d.c4*y+d.c5*Math.pow(y,2)+d.c6*x*y
                zList.push(z)
            })
        })

        var zList2=zList.map(function(val){
            return val*coef/1000
        })

        return [xList,yList,zList2]
    }

    function render(data,id,title){
        console.log(data[2])
        var zmax=Math.max.apply(null,data[2]).toFixed(1)
        console.log(zmax)
        var trace1 = {
            x:data[0], y: data[1], z: data[2],
            /*
            colorscale: [
              [0, 'rgb(255, 0, 0)'],
              [zmax/2, 'rgb(0, 255, 0)'],
              [zmax, 'rgb(0, 0, 255)']
            ],
            */
            //colorscale: 'YIOrRd',
            type: 'mesh3d'
        };

        var data = [trace1];
        var layout = {
            margin: {
            l: 0,
            r: 0,
            b: 0,
            t: 0
          },
          title:title,
          showlegend:true,
          xaxis:{
            title:"chilled water leaving temperature[C]",
            titlefont: {
                size: 18,
                color: '#7f7f7f'
            }
          },
          yaxis:{
            title:"condensing fluid entering temperature[C]",
            titlefont: {
                size: 18,
                color: '#7f7f7f'
            }
          }
        };
        Plotly.newPlot(id, data, layout);

        var plot=document.getElementById(id);

        plot.on('plotly_click', function(data){
            var url = data.points.map(function(d){
                console.log(d);
                //return '/hvac/api/'+d.data.name[d.pointIndex]
            })
            //scatter3d(url)
        });

    };

    
}

function test(){
        Plotly.d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv', function(err, rows){
        function unpack(rows, key) {
          return rows.map(function(row) { return row[key]; });
        }
          
        var z_data=[ ]
        for(i=0;i<24;i++)
        {
          z_data.push(unpack(rows,i));
        }

        console.log(z_data)
        var data = [{
                   z: z_data,
                   type: 'surface'
                }];
          
        var layout = {
          title: 'Mt Bruno Elevation',
          autosize: false,
          width: 500,
          height: 500,
          margin: {
            l: 65,
            r: 50,
            b: 65,
            t: 90,
          }
        };
        Plotly.newPlot('myDiv', data, layout);
        });
    }