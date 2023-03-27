#include <stdio.h>
#include <stdlib.h>
#include <Windows.h>
#include <math.h>

int LabStats(); //Statistics Function

void color(int Background, int Text); //Function for coloring text in console

enum colors //List of colors for color function
{
 	BLACK=0,
	BLUE=1,
 	GREEN=2,
 	CYAN=3,
 	RED=4,
 	MAGENTA=5,
 	YELLOW=14,
 	WHITE=15
};

int main()
{
    int APP, again_APP;
    
    color(BLACK,BLUE);
    printf("\n\t\t\t\t\t         :::::::::: :::::::::   ::::::::");
    printf("\n\t\t\t\t\t        :+:        :+:    :+: :+:    :+:");
    printf("\n\t\t\t\t\t       +:+        +:+    +:+ +:+        ");
    printf("\n\t\t\t\t\t      :#::+::#   +#++:++#+  +#+         ");
    printf("\n\t\t\t\t\t     +#+        +#+        +#+          ");
    printf("\n\t\t\t\t\t    #+#        #+#        #+#    #+#    ");
    printf("\n\t\t\t\t\t   ###        ###         ########      ");
    color(BLACK,WHITE);
    
    //ASCII ART
	printf("\n\n\n");
	
	color(BLACK,RED);
	
	printf("\n        :::            :::     :::::::::   :::::::: ::::::::::: ::: ::::::::::: ::::::::           ::::::::   ::::::::");
	printf("\n       :+:          :+: :+:   :+:    :+: :+:    :+:    :+:   :+: :+:   :+:    :+:    :+:         :+:    :+: :+:    :+:");
	printf("\n      +:+         +:+   +:+  +:+    +:+ +:+           +:+  +:+   +:+  +:+    +:+                +:+        +:+    +:+ ");
	printf("\n     +#+        +#++:++#++: +#++:++#+  +#++:++#++    +#+ +#++:++#++: +#+    +#++:++#++         +#+        +#+    +:+  ");
	printf("\n    +#+        +#+     +#+ +#+    +#+        +#+    +#+ +#+     +#+ +#+           +#+         +#+        +#+    +#+   ");
	printf("\n   #+#        #+#     #+# #+#    #+# #+#    #+#    #+# #+#     #+# #+#    #+#    #+#         #+#    #+# #+#    #+#    ");
	printf("\n  ########## ###     ### #########   ########     ### ###     ### ###     ########           ########   ########      ");
	
	printf("\n\n");
	
	printf("\n\t\t\t                                                       ___");
	printf("\n\t\t\t                                                   ,o88888 ");
	printf("\n\t\t\t                                                ,o8888888' ");
	printf("\n\t\t\t                          ,:o:o:oooo.        ,8O88Pd8888'  ");
	printf("\n\t\t\t                      ,.::.::o:ooooOoOoO. ,oO8O8Pd888""    ");
	printf("\n\t\t\t                    ,.:.::o:ooOoOoOO8O8OOo.8OOPd8O8O´      ");
	printf("\n\t\t\t                   , ..:.::o:ooOoOOOO8OOOOo.FdO8O8'        ");
	printf("\n\t\t\t                  , ..:.::o:ooOoOO8O888O8O,COCOO´          ");
	printf("\n\t\t\t                 , . ..:.::o:ooOoOOOO8OOOOCOCO'            ");
	printf("\n\t\t\t                  . ..:.::o:ooOoOoOO8O8OCCCC*o             ");
	printf("\n\t\t\t                     . ..:.::o:ooooOoCoCCC*o:o             ");
	printf("\n\t\t\t                     . ..:.::o:o:,cooooCo*oo:o:            ");
	printf("\n\t\t\t                  `   . . ..:.:cocoooo*'o:o:::'            ");
	printf("\n\t\t\t                  .`   . ..::ccccoc*'o:o:o:::'             ");
	printf("\n\t\t\t                 :.:.    ,c:cccc*':.:.:.:.:.'              ");
	printf("\n\t\t\t               ..:.:*'`::::c:*'..:.:.:.:.:.'               ");
	printf("\n\t\t\t             ...:.'.:.::::*'    . . . . .'                 ");
	printf("\n\t\t\t            .. . ....:.*' `   .  . . ''                    ");
	printf("\n\t\t\t          . . . ....'´                                     ");
	printf("\n\t\t\t          .. . .´'       -hrr-                             ");
	printf("\n\t\t\t         .                                                 ");
	
	color(BLACK,WHITE);
    
    color(BLACK,RED);
    printf("\n\n\n=============================================  Welcome to LabStats Co.!  =============================================");
    printf("==========================================================================================================================");
	color(BLACK,WHITE);
    printf("\n\nThis app can be used to solve statistical data for classical mechanics experiments.");
    color(BLACK,RED);
	printf("\n\nLabStats Co.");
	color(BLACK,WHITE);
    printf("is a dedicated APP to solve lineal correlation and regression calculus for your experiments.");
    printf("\n\nHere you can do the correlation and regression calculations of your laboratory data.\n\n");
    
    system("pause");
    system("cls");
    
    LabStats();
    
    do
    {
    	do
    	{
			printf("\n\nDo you need to use this programm again?  1) Yes   2) No\n");
			printf("Selection: ");
			scanf("%d", &again_APP);
    	}
    	while(again_APP!=1 && again_APP!=2);
    	
		if(again_APP==1)
		{
		    system("cls");
		    LabStats();
		}
		else if(again_APP==2)
		{
			system("cls");
			printf("\n\n\t\tThank you for using FCP LabStats, see you soon!\n\n");
			color(BLACK,BLUE);
			printf("\n\t\t     ::::::::::: :::    ::: :::    :::");
			printf("\n\t\t        :+:     :+:    :+: :+:    :+: ");
			printf("\n\t\t       +:+     +:+    +:+  +:+  +:+   ");
			printf("\n\t\t      +#+     +#++:++#++   +#++:+     ");
			printf("\n\t\t     +#+     +#+    +#+  +#+  +#+     ");
			printf("\n\t\t    #+#     #+#    #+# #+#    #+#     ");
			printf("\n\t\t   ###     ###    ### ###    ###      ");
			color(BLACK,WHITE);
			printf("\n");
		}
	}
	while(again_APP==1);
	
    return 0;
}

int LabStats()
{
	int n, i, j, k, l, m, CONFIRM_DATA; //Step 1-3 vars n=number of ordered pairs, i,j,k,l,m=counters for arrays, confirm data
	float x[100], y[100]; //Step 1-3 vars
	
	// x, y, xy=x*y, p = promedio de algo, sum = suma de algo, xx=x^2, yy=y^2
	float xx[100], yy[100], xy[100]; //First calculations with data
	float px, py, pxx, pyy, pxy; //Average of X and Y
	float sum_X=0, sum_Y=0, sum_XX=0, sum_YY=0, sum_XY=0; //Sums of the values
	float S, I, r_xy, r_sqrd, devY[100], Ysum_var, Ysigma2, Ysigma, devX[100], Xsum_var, Xsigma2, Xsigma; //Slope and Intersection
	
	printf("\nProcessing...");
	
	//Subrutina necesaria para leer todos los datos de los pares ordenados obtenidos en una estadística
    do 
    {
	    //Determinate the number of ordered pairs "n"
	    color(BLACK,CYAN);
	    printf("\nStep 1: Introduce the number of ordered pairs that you are using\n\n");
	    color(BLACK,WHITE);
        scanf("%d", &n);
        //Ask for the values of X, then operate average and total sum
        color(BLACK,CYAN);
	    printf("\nStep 2: Digit %d data corresponding to X values\n\n", n);
	    color(BLACK,WHITE);
        for(i=0;i<n;i++)
            scanf("%f", &x[i]);
        //Ask for the values of Y, then operate average and total sum
        color(BLACK,CYAN);
        printf("\nStep 3: Digit %d data corresponding to Y values\n\n", n);
        color(BLACK,WHITE);
        for(i=0;i<n;i++)
            scanf("%f", &y[i]);
        //Printing (x,y) values and others to confirm data
        printf("\nDATA COLLECTION...");
        for(i=0;i<n;i++)
            printf("\n(%.4f, %.4f)", x[i], y[i]);
        //printf("\nSum of X: %.4f\nSum of Y: %.4f\nAverage of X: %.4f\nAverage of Y: %.4f", sum_X, sum_Y, px, py);
        //Ask to confirm data
        do
        {
        	printf("\n\nDo you want to confirm these data?  1) Yes   2) No\n");
        	scanf("%d", &CONFIRM_DATA);
		}
		while(CONFIRM_DATA!=1 && CONFIRM_DATA!=2);
    }
    while(CONFIRM_DATA==2);

    //Do X^2, Y^2, XY and the sums and averages
    color(BLACK,CYAN);
    printf("\nStep 4: Get X^2, Y^2 and XY values\n");
    color(BLACK,WHITE);
    
    //X^2 "xx[j]"
    for(i=0,j=0;i<n && j<n;i++,j++)
        xx[j]=pow(x[i],2);
    for(j=0;j<n;j++)
        printf("\nX^2: %.4f", xx[j]);
    
    //Y^2 "yy[k]"
    for(i=0,k=0;i<n && k<n;i++,k++)
        yy[k]=pow(y[i],2);
    for(k=0;k<n;k++)
        printf("\nY^2: %.4f", yy[k]);
    
    //XY "xy[l]"
    for(i=0,l=0;i<n && l<n;i++,l++)
        xy[l]=x[i]*y[i];
    for(l=0;l<n;l++)
        printf("\nXY: %.4f", xy[l]);
    
    color(BLACK,CYAN);
    printf("\n\nStep 5: Get all sums and averages\n");
    color(BLACK,WHITE);
    //Now do the sum and average of values of X
    for(i=0;i<n;i++)
        sum_X+=x[i];
    px=sum_X/n;    
    printf("\nSum of X values: %.4f\nAverage of X values: %.4f\n", sum_X, px);
    
    //Now do the sum and average of values of Y
    for(i=0;i<n;i++)
        sum_Y+=y[i];
    py=sum_Y/n;
    printf("\nSum of Y values: %.4f\nAverage of Y values: %.4f\n", sum_Y, py);
    
    //Do X^2, Y^2, XY and the sums and averages
    for(j=0;j<n;j++)  //For xx[j]
        sum_XX+=xx[j];
    pxx=sum_XX/(n);
    printf("\nSum of X^2 values: %.4f\nAverage of X^2: %.4f\n", sum_XX, pxx);
    
    for(k=0;k<n;k++)  //For yy[k]
        sum_YY+=yy[k];
    pyy=sum_YY/n;
    printf("\nSum of Y^2 values: %.4f\nAverage of Y^2: %.4f\n", sum_YY, pyy);
    
    for(l=0;l<n;l++)  //For xy[l]
        sum_XY+=xy[l];
    pxy=sum_XY/n;
    printf("\nSum of XY values: %.4f\nAverage of XY: %.4f\n", sum_XY, pxy);
    
    //Printing (x,y) values and others to confirm data and visualizae it, again...
    printf("\nDATA COLLECTION...");
    for(i=0, j=0;i<n && j<n;i++, j++)
        printf("\n(%.4f, %.4f)", x[i], y[j]);
    
    color(BLACK,CYAN);
    printf("\n\nStep 6: Get the variance and standard deviation\n");
    color(BLACK,WHITE);

	//Calculating variance and standard deviation for Y
    for(m=0, i=0;m<n && i<n;m++, i++)
        devY[m]=pow((y[i]-py), 2);
    for(m=0;m<n;m++)
        Ysum_var+=devY[m];
    Ysigma2=Ysum_var/(n-1); 
    Ysigma=sqrt(Ysigma2);
    //Calculating variance and standard deviation for X
    for(m=0, i=0;m<n && i<n;m++, i++)
        devX[m]=pow((x[i]-px), 2);
    for(m=0;m<n;m++)
        Xsum_var+=devX[m];
    Xsigma2=Xsum_var/(n-1); 
    Xsigma=sqrt(Xsigma2);
    
    printf("\nVariance of X: %.4f\nStandard deviation of X: %.4f\nVariance of Y: %.4f\nStandard deviation of Y: %.4f", Xsigma2, Xsigma, Ysigma2, Ysigma);
    
    //Calculate the slope of f(x) and the intersection with "y" axis of f(x) and print them
	color(BLACK,CYAN);    
    printf("\n\nStep 7: Get all your data for your stimation equation\n");
    color(BLACK,WHITE);
    S=(n*sum_XY-sum_X*sum_Y)/(n*sum_XX-sum_X*sum_X);
    I=(sum_XX*sum_Y-sum_X*sum_XY)/(n*sum_XX-sum_X*sum_X);
    printf("\nSlope: %.4f\nIntersection with Y: %.4f", S, I);
	
	//Calculate r^2 and r coefficients
	color(BLACK,CYAN);
	printf("\n\nStep 8: Get your determination and correlation coefficients\n");
	color(BLACK,WHITE);
	r_xy=(sum_XY-n*px*py)/(sqrt(sum_XX-n*px*px)*sqrt(sum_YY-n*py*py));
    r_sqrd=r_xy*r_xy;
    printf("\nDetermination coefficient (r^2): %.4f\nCorrelation coefficient (r): %.4f", r_sqrd, r_xy);
    
    //Interpretation of r_xy
    if(r_xy>=0.0 && r_xy<=0.10)
    {
		printf("\nX and Y values have a ");
		color(BLACK,RED);
		printf("non-existent");
		color(BLACK,WHITE);
		printf(" correlation");
	} else if(r_xy>0.10 && r_xy<=0.29)
	{
		printf("\nX and Y values have a ");
		color(BLACK,YELLOW);
		printf("weak");
		color(BLACK,WHITE);
		printf(" correlation");
	} else if(r_xy>=0.30 && r_xy<=0.50)
	{
		printf("\nX and Y values have a ");
		color(BLACK,GREEN);
		printf("moderate");
		color(BLACK,WHITE);
		printf(" correlation");
	} else if(r_xy>0.50 && r_xy<=1.00)
	{
		printf("\nX and Y values have a ");
		color(BLACK,BLUE);
		printf("strong");
		color(BLACK,WHITE);
		printf(" correlation");
	}
	
	//Writting a stimation equation
	color(BLACK,CYAN);
    printf("\n\nStep 9: Get your stimation equation\n");
    color(BLACK,WHITE);
    printf("\n\t\ty=%.2fx+%.2f", S, I);
    
	return 0;
}
	
void color(int Background, int Text) //Function to change the background and text color
{   
    HANDLE Console=GetStdHandle(STD_OUTPUT_HANDLE); //It takes the console
    
    int New_Color=Text+(Background*16); //It is necessary to make this calculus in order to change the colors

    SetConsoleTextAttribute(Console, New_Color); //Saves the color changes on console
}
