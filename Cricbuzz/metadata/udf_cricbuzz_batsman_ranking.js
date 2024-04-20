function transform(line){
	var values = line.split(',');
	var obj = new Object();
	obj.rank = values[0];
	obj.name = values[1];
	obj.country = values[2];
	obj.rating = values[3];
	obj.points = values[4];
	obj.lastUpdated = values[5];
	obj.countryId = values[6];
	obj.avg = values[7];
	
	var jsonString = JSON.stringify(obj);
	return jsonString;
}