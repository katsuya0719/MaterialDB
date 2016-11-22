app.directive('d3Scatters',['d3Service','$window',function(d3Service,$window){
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
		        		color = d3.scale.category10();
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
		        		d.consumption = +d.wattage;
		        		d.flux = +d.flux;
		        	});

		        	x.domain(d3.extent(data, function(d){ return d.consumption; })).nice();
		        	y.domain(d3.extent(data, function(d){ return d.flux; })).nice();

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
		        		.text("Consumption[W]");

		        	svg.append("g")
		        		.attr("class","y axis")
		        		.call(yAxis)
		        		.append("text")
		        		.attr("class", "label")
		        		.attr("transform","rotate(-90)")
		        		.attr("y",20)
		        		.attr("dy", ".71em")
		        		.style("text-anchor","end")
		        		.text("Flux[lm]");

		        	var div=d3.select("body").append("div")
		        		.attr("class", "tooltip")
		        		.style("opacity", 0)

		        	svg.selectAll(".dot").data(data).enter()
		        		.append("circle")
		        		.attr("class","dot")
		        		.attr("r", 5)
		        		.attr("cx", function(d){ return x(d.consumption); })
		        		.attr("cy", function(d){ return y(d.flux); })
		        		.style("fill", function(d){return color(d.lamp_type); })
		        		.on("mouseover",function(d){
		        			div.transition()
		        				.duration(200)
		        				.style("opacity", .9);
		        			div.html(d.title + "<br/>mercury:" + d.mercury + "mg")
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
		        };
			});
		}
	};
}]);