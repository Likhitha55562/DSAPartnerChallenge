# Day 1 – DSA Practice
# Day 1 – Pseudocode & Flowcharts

## 1. Leap Year Check

START  
INPUT year  
IF (year % 4 == 0) AND (year % 100 != 0 OR year % 400 == 0)  
    PRINT "Leap Year"  
ELSE  
    PRINT "Not Leap Year"  
END IF  
END
### Flowcharts

        Start
          |
      Input Year
          |
  -------------------------
  | Year %4==0 AND        |
  | (Year %100!=0 OR      |
  | Year %400==0) ?       |
  -------------------------
       /        \
     Yes        No
      |          |
 Print Leap   Print Not
    Year      Leap Year
      |
     End

     
---

## 2. Sum of Two Numbers
### Pseudocode

START  
INPUT num1  
INPUT num2  
sum = num1 + num2  
PRINT sum  
END

### Flowchart

      Start
        |
   Input num1
   Input num2
        |
   sum = num1 + num2
        |
     Print sum
        |
        End
        
---

## 3. Multiplication Table

### Pseudocode
START  
INPUT number  
FOR i = 1 TO 10  
    result = number * i  
    PRINT number x i = result  
END FOR  
END

### Flowchart

        Start
          |
     Input number
          |
        i = 1
          |
     ----------- 
     | i <= 10? |
     -----------
      /       \
    Yes       No
     |         |
Print number*i |
     |         |
   i = i + 1   |
     |         |
     ----------- 
          |
          End


---

## 4. HCF and LCM

### Pseudocode

START  
INPUT a  
INPUT b  
temp1 = a  
temp2 = b  
WHILE b ≠ 0  
    remainder = a % b  
    a = b  
    b = remainder  
END WHILE  
HCF = a  
LCM = (temp1 * temp2) / HCF  
PRINT HCF  
PRINT LCM  
END

### Flowchart

        Start
          |
      Input a, b
          |
     temp1 = a
     temp2 = b
          |
     ------------
     | b != 0 ? |
     ------------
      /       \
    Yes       No
     |         |
r = a % b      |
a = b          |
b = r          |
     |         |
     ----------- 
          |
      HCF = a
          |
 LCM = (temp1*temp2)/HCF
          |
   Print HCF, LCM
          |
          End


---

## 5. Sum Until 'x'

### Pseudocode

START  
sum = 0  
REPEAT  
    INPUT value  
    IF value == 'x'  
        BREAK  
    END IF  
    sum = sum + value  
UNTIL value == 'x'  
PRINT sum  
END

### Flowcharts

        Start
          |
       sum = 0
          |
      Input value
          |
     -------------
     | value = x? |
     -------------
      /        \
    Yes        No
     |          |
 Print sum   sum = sum + value
     |          |
    End     Input value
                |
             Repeat
