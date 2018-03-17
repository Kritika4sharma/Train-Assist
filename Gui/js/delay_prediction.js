var $form           = $('.js-train-prediction-form');
var $trainNumberInput = $('.js-train-number-input');
var $errorsOutput  = $('.js-errors');
var $dateInput   = $('.js-date-input');
var $hourOutput  = $('.js-delay');
var $confidence   = $('.js-confidence')

function compute() {
  var trainNumber    = $trainNumberInput.val();
  var date           = $dateInput.val();

  if( trainNumber == "" ) {
    $errorsOutput.html("Please enter a train number");
  }
  
 var date1 = date.toString();
 var train_string = trainNumber.toString()
 //var date_string = new Date(date1).toDateString("yyyy-MM-dd");
 var input = train_string + " " + date1

// call python script
//console.log(date_string);
  //response= runPyScript(input);
  response = "more than 4 hours"
  console.log(input);
  // re
  $hourOutput.html(response);
  $confidence.html(response);
};

function runPyScript(input){
    var obj = $.ajax({
        type: "POST",
        url: "/model_v1.py",
        async: false,
        data: { param: input }
    });
    return obj.responseText;
}

$(document).ready(function() {
  $dateInput.on('blur', compute); 

  // $trainNumberInput.on('keyup', function() {
    
  // });

});
  