#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
using namespace std;
vector<string> line[16384];
int main()
{
	ifstream in("D:\\fin.csv");  
	if (! in.is_open())  
	{ 
		cout << "Error opening file";
		return 0; 
	}
	char temp1;
	char temp2;
	char temp3; 
	string s="AA";
 	for(int i=0;i<1000;i++)
	{
		for(int j=0;j<9445;j++)
		{
			in>>temp1;
			in>>temp2;
			in>>temp3;
			s[0]=temp1;
			s[1]=temp2;
			s[2]='\0';
			line[j].push_back(s);
		}
	}
	
	vector<string> vtemp; 
	for(int i=0;i<9445;i++)
	{
		vtemp.clear();
		for(int j=0;j<1000;j++)
		{
			if(line[i][j][0]!=line[i][j][1])
			{
				char ch0[3];
				char ch2[3];
				ch0[0]=line[i][j][0];
				ch0[1]=line[i][j][0];
				ch0[2]='\0';
				ch2[0]=line[i][j][1];
				ch2[1]=line[i][j][1];
				ch2[2]='\0';
				vtemp.push_back(ch0);
				vtemp.push_back(line[i][j]);
				vtemp.push_back(ch2);
				break;
			}
		}
		for(int j=0;j<1000;j++)
		{
			for(int k=0;k<vtemp.size();k++)
			{
				if(line[i][j]==vtemp[k])
				{
					stringstream ss;
					ss<<k; 
					string s1 = ss.str();
					line[i][j]=s1;
					break;
				}
			}
		}
	}
	ofstream out("D:\\res.csv");
	for(int i=0;i<1000;i++)
	{
		for(int j=0;j<9445;j++)
		{
			out<<line[j][i]<<",";
		}
		out<<"\n";
	}
	in.close();
	out.close();
}