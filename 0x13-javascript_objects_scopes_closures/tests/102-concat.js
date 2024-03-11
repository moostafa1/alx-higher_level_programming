const fs = require('fs');

// Check if exactly three file paths are provided as arguments
if (process.argv.length !== 5) {
    console.error('Usage: node concat-files.js <source-file-1> <source-file-2> <destination-file>');
    process.exit(1);
}

// Get the file paths from the command line arguments
const [, , sourceFilePath1, sourceFilePath2, destinationFilePath] = process.argv;

// Read the contents of the first source file
fs.readFile(sourceFilePath1, 'utf8', (err1, data1) => {
    if (err1) {
        console.error(`Error reading file ${sourceFilePath1}:`, err1);
        process.exit(1);
    }

    // Read the contents of the second source file
    fs.readFile(sourceFilePath2, 'utf8', (err2, data2) => {
        if (err2) {
            console.error(`Error reading file ${sourceFilePath2}:`, err2);
            process.exit(1);
        }

        // Concatenate the contents of the two files
        const concatenatedData = data1 + data2;

        // Write the concatenated data to the destination file
        fs.writeFile(destinationFilePath, concatenatedData, 'utf8', (err) => {
            if (err) {
                console.error(`Error writing to file ${destinationFilePath}:`, err);
                process.exit(1);
            }
            console.log(`Concatenated data written to ${destinationFilePath}`);
        });
    });
});
