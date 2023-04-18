#include <stdio.h>
#include <stdlib.h>
#include "libxl.h"

// Funtion to calculate linear regression and return slope and intercept
void linearRegression(data[], int nrows, double *slope, double *intercept) {
    double sumX = 0.0, sumY = 0.0, sumXY = 0.0, sumXX = 0.0;
    
    for (int i = 0; i < n; i++) {
        sumX += data[i].x;
        sumY += data[i].y;
        sumXY += data[i].x * data[i].y;
        sumXX += data[i].x * data[i].x;
    }
    
    double denom = n * sumXX - sumX * sumX;
    
    if (denom == 0) {
        // Unable to calculate linear regression
        *slope = 0.0;
        *intercept = 0.0;
        return;
    }
    
    *slope = (n * sumXY - sumX * sumY) / denom;
    *intercept = (sumY - *slope * sumX) / n;
}

int main()
{
    int i, j;
    int nrows, ncols;
    const char* filename = "data.xlsx";
    Book* book;
    Sheet* sheet;
    const char* cell_value;
    double data[100][2]; // Storage matrix for ordered pairs (x,y)
    double sum_x = 0, sum_y = 0, sum_xy = 0, sum_x2 = 0;
    
    book = xlCreateBook();
    if (book == NULL) {
        printf("Error: Unable to create the file.\n");
        return 1;
    }
    
    if (xlBookLoad(book, filename) == 0) {
        printf("Error: Unable to open the file.\n");
        return 1;
    }
    
    sheet = xlBookGetSheet(book, 0); // Obtain sheet 0 from the book
    if (sheet == NULL) {
        printf("Error: Unable to obtain the sheet from the book.\n");
        return 1;
    }
    
    nrows = xlSheetLastRow(sheet);
    ncols = xlSheetLastCol(sheet);
    
    for (i = 0; i < nrows; i++) {
        for (j = 0; j < ncols; j++) {
            cell_value = xlSheetReadStr(sheet, i, j, NULL); // Read cell value
            data[i][j] = atof(cell_value); // Store value as a number
        }
    }
    
    xlBookRelease(book);
    
    // Data is stored in "data" matrix
    
    double slope, intercept;
    
    // Calculate necessary sums for linear regression
    linearRegression(data[], nrows, &slope, &intercept);
  
    printf("The slope of the linear regression line is: %lf\n", slope);
    printf("The intercept of the linear regression line is: %lf\n", intercept);
    
    return 0;
}
