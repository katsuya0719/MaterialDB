app.directive('glassScatters',['d3Service','$window',function(d3Service,$window){
	return{
		restrict: 'EA',
		scope:{
			data:'=',
		},
		link: function(scope,ele,attrs){
			d3Service.d3().then(function(d3){
				var margin = parseInt(attrs.margin)||50
				var svg=d3.select(ele[0])
					.append('svg')
					.style('width','100%');

				window.onresize=function(){
					scope.$apply();
				};

		        scope.$watch(function(){
		        	return angular.element($window)[0].innerWidth;
		        	}, function(){
		        		scope.render(scope.data);
		        });

		        scope.$watch('data',function(newVals,oldVals){
		        	return scope.render(newVals);
		        }, true);

		        scope.render = function(data){
		        	svg.selectAll('*').remove();
		        	if(!data) return;
		        	var width = d3.select(ele[0]).node().offsetWidth,
		        		height = 500,
		        		color = d3.scale.category20();
		        	console.log(data)

		        	var x = d3.scale.linear().range([0,width-margin]),
		        		y = d3.scale.linear().range([height-margin,0]), 
		        		xAxis = d3.svg.axis().scale(x).orient("bottom"),
		        		yAxis = d3.svg.axis().scale(y).orient("right"),
		        		ylen=height-margin;
		        		//xScale = d3.scale.linear().domain([0,d3.max(data, function(d){
		        		//	return d.score;
		        		//})]).range([0,width]);

		        	data.forEach(function(d){
		        		//new1 = +d.tsol
		        		//new2 = +d.tvis
		        		d.tsol = floatFormat(+d.tsol,2);
		        		d.tvis = floatFormat(+d.tvis,2);
		        		d.thickness = floatFormat(+d.thickness,1);
		        		d.thick = Math.round(+d.thickness);
		        	});

		        	//x.domain(d3.extent(data, function(d){ return d.tsol; })).nice();
		        	x.domain([0,1]);
		        	y.domain([0,0.1]);

		        	svg.attr('height',height);

		        	svg.append("g")
		        		.attr("class","x axis")
		        		.attr("transform", "translate(0," +ylen+ ")")
		        		.call(xAxis)
		        		.append("text")
		        		.attr("class", "label")
		        		.attr("x", width)
		        		.attr("y",-6)
		        		.style("text-anchor","end")
		        		.text("Solar Transmittance");

		        	svg.append("g")
		        		.attr("class","y axis")
		        		.call(yAxis)
		        		.append("text")
		        		.attr("class", "label")
		        		.attr("transform","rotate(-90)")
		        		.attr("y",20)
		        		.attr("dy", ".71em")
		        		.style("text-anchor","end")
		        		.text("Visual Light Transmittance");

		        	var div=d3.select(".dot").append("div")
		        		.attr("class", "tooltip")
		        		.style("opacity", 0)

		        	svg.selectAll(".dot").data(data).enter()
		        		.append("circle")
		        		.attr("class","dot")
		        		.attr("r", 5)
		        		.attr("cx", function(d){ return x(d.tsol); })
		        		.attr("cy", function(d){ return y(d.tvis); })
		        		.style("fill", function(d){return color(d.thick); })
		        		.on("mouseover",function(d){
		        			div.transition()
		        				.duration(200)
		        				.style("opacity", .9);
		        			div.html(d.title + "<br/>Thickness:" + d.thickness + "[mm]" + "<br/>VLT:" + d.tvis + "<br/>g:"　+d.tsol )
		        				.style("left", (d3.event.pageX) + "px")
		        				.style("top", (d3.event.pageY) + "px");
		        		})
		        		.on("mouseout", function(d){
		        			div.transition()
		        				.duration(500)
		        				.style("opacity", 0);
		        		});

		        	var legend = svg.selectAll(".legend")
		        		.data(color.domain())
		        		.enter().append("g")
		        		.attr("class","legend")
		        		.attr("transform", function(d,i){ return "translate(0," +i*20+ ")"; });

		        	legend.append("rect")
		        		.attr("x", width - 18)
		        		.attr("width", 18)
		        		.attr("height", 18)
		        		.style("fill", color);

		        	legend.append("text")
		        		.attr("x", width-24)
		        		.attr("y", 9)
		        		.attr("dy", ".35em")
		        		.style("text-anchor","end")
		        		.text(function(d){ return d; });

		        	function floatFormat( number, n ) {
						var _pow = Math.pow( 10 , n ) ;

						return Math.round( number * _pow ) / _pow ;
}
		        };
			});
		}
	};
}]);