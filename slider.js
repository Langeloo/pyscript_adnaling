var lowerSlider = document.querySelector('#lower'),
   upperSlider = document.querySelector('#upper'),
   lower2Slider = document.querySelector('#lower2'),
   upper2Slider = document.querySelector('#upper2'),
   lowerVal = parseInt(lowerSlider.value);
   upperVal = parseInt(upperSlider.value);
   lower2val = parseInt(lower2Slider.value);
   upper2val = parseInt(upper2Slider.value);

upperSlider.oninput = function() {
   lowerVal = parseInt(lowerSlider.value);
   upperVal = parseInt(upperSlider.value);
   
   if (upperVal < lowerVal + 4) {
      lowerSlider.value = upperVal - 4;
      
      if (lowerVal == lowerSlider.min) {
         upperSlider.value = 4;
      }
   }
   document.getElementById("labelupper").innerHTML = this.value;
   document.getElementById("labellower").innerHTML = lowerSlider.value;
};


lowerSlider.oninput = function() {
   lowerVal = parseInt(lowerSlider.value);
   upperVal = parseInt(upperSlider.value);
   
   if (lowerVal > upperVal - 4) {
      upperSlider.value = lowerVal + 4;
      
      if (upperVal == upperSlider.max) {
         lowerSlider.value = parseInt(upperSlider.max) - 4;
      }

   }
   document.getElementById("labellower").innerHTML = this.value;
   document.getElementById("labelupper").innerHTML = upperSlider.value;
};

upper2Slider.oninput = function() {
   lower2val = parseInt(lower2Slider.value);
   upper2val = parseInt(upper2Slider.value);

   if (upper2val < lower2val + 4) {
      lower2Slider.value = upper2val - 4;

      if (lower2val == lower2Slider.min) {
         upper2Slider.value = 4;
      }
   }
   document.getElementById("labelupper2").innerHTML = this.value;
   document.getElementById("labellower2").innerHTML = lower2Slider.value;
}

lower2Slider.oninput = function() {
   lower2val = parseInt(lower2Slider.value);
   upper2val = parseInt(upper2Slider.value);

   if (lower2val > upper2val - 4) {
      upper2Slider.value = lower2val + 4;

      if (upper2val == upper2Slider.max) {
         lower2Slider.value = parseInt(upper2Slider.max) - 4;
      }
   }
   document.getElementById("labellower2").innerHTML = this.value;
   document.getElementById("labelupper2").innerHTML = upper2Slider.value;
}