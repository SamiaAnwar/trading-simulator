export const pointColors = (x1, x2, y2) => {
    //x1, y1 = all dates in the month
    //x2, y2 = dates where trade occurred, trade action 
    const colors = [];
    var traded = false;
    var j = 0; 
    for (let i = 0; i < x1.length; i++){
        traded = x2[j] === x1[i];
        if (traded && y2[j]===1) {
            colors.push('#FF0000'); 
            j++; 
        }
        else if(traded && y2[j]===0){
            colors.push('#0000FF');
            j++; 
        }
        else {
            colors.push('#00FF00'); 
        }
    };
    return colors; 
}


export const get_attribute = (data, attribute, groupby, groupbyVal) => {
    const res = []; 
    for (let i = 0; i < data.length; i++){
        if (data[i][groupby] === groupbyVal) {
            res.push(data[i][attribute]); 
        }
    }
    return attribute; 
}