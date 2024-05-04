Data_Parse.py 
Powershell script that parses through file, grabs information, makes a new file, and names it with proper date etc. 

	$file = Read-Host -Prompt 'Give me the path of backups from this week' #the file you copied the bacula info to 
	$timestamp = Get-Date -Format "yyyy_MM_dd"
	$destinationFile = "C:\Users\jose.claudio\Documents\Backup03\${timestamp}_failed.txt" # What the file's name will be
	$keyword = "F.*f|f.*F" # replace with the text you want to search for
	
	Get-Content $file | Where-Object { $_ -match $keyword } | Out-File $destinationFile -Append
	
	
	This one will give the format I want, solving the filename issue ex: XXXX_XX_XX

