#include <stdio.h>
#include <stdlib.h>

int check_authentication() {
	int auth_flag = 0;
	char password_buffer[16];
	printf("Enter password\n");
	scanf("%s", password_buffer);
	/* password_buffer ok? => auth_flag = 1 */
	return auth_flag;
}


int main(int argc, char* argv[]) {
	if (check_authentication())
	{
		printf("Oh you got me! Here the flag: FLAG{PwNiNg_Is_FuN_xD}\n");
	}
	else
	{
		printf("Password not valid!\n");
	}	
	return 0;
}



