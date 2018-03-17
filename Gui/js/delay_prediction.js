var $form           = $('.js-train-prediction-form');
var $trainNumberInput     = $('.js-train-number-input');
var $dateInput   = $('.js-date-input');
var $hourOutput  = $('.js-delay');
var $errorsOutput   = $('.js-errors');


function compute() {
  var trainNumber     = $trainNumberInput.val();
  var date           = $dateInput.val();

  if( trainNumber == "" ) {
    $errorsOutput.html("Please enter a train number");
  }

  //var minutesInDecimal  = (minutes / 60).toFixed(2)
  
  // var convertedHours    = parseFloat(hours);
  // var convertedMinutes  = parseFloat(minutesInDecimal);
  // var total             = convertedHours += convertedMinutes;
 var date_string = date.toString();
 var train_string = trainNumber.toString()
 var input = train_string + " " + date_string

// call python script

  //response= runPyScript(input);
  response = "more than 4 hours"
  console.log(response);
  // re
  $hourOutput.html(response);
};

function runPyScript(input){
    var jqXHR = $.ajax({
        type: "POST",
        url: "/model_v1.py",
        async: false,
        data: { param: input }
    });
    // format response text
    return jqXHR.responseText;
}
function limitMinutesLength() {
  var maxChars = 2;

  if ($minutesInput.val().length > maxChars) {
      $minutesInput.val($minutesInput.val().substr(0, maxChars));
  };
};

function limitMinutesRange() {
  var maxMinutes = 59;

  if( $minutesInput.val() > 59 || $minutesInput.val() < 0) {
    $errorsOutput.html("Minutes must be between 0 and 59");
  } else {
    $errorsOutput.html("");
  };
}

$(document).ready(function() {
  $trainNumberInput.on('blur', compute);
  

  $trainNumberInput.on('keyup', function() {
    //limitMinutesLength();
    
  });

});
  