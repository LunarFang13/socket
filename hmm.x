struct numbers{
     int a[100];
};


program ADD_PROG{
   version ADD_VERS{
       int add(numbers)=1;
   }=1;
   
}=0x4562877;

program GRT_PROG{
   version GRT_VERS{
       int grt(numbers)=1;
   }=1;
}=0x4562878;

program SINE_PROG{
   version SINE_VERS{
       int sine(numbers)=1;
   }=1;
}=0x4562879;

program FACT_PROG{
   version FACT_VERS{
       int fact(numbers)=1;
   }=1;
}=0x4562876;

program REV_PROG{
   version REV_VERS{
       int rev(numbers)=1;
   }=1;
}=0x4562875;

program SUMD_PROG{
   version SUMD_VERS{
       int sumd(numbers)=1;
   }=1;
}=0x4562874;
