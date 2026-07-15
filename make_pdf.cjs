const fs = require('fs');
const PDFDocument = require('pdfkit');

const doc = new PDFDocument();
doc.pipe(fs.createWriteStream('public/magazines/Mini_Research_Reports.pdf'));

// Page 1
doc.fontSize(24).text('Mini Research Reports', { align: 'center' });
doc.moveDown();
doc.fontSize(14).text('A personal compilation', { align: 'center' });
doc.addPage();

// Page 2
doc.fontSize(20).text('1. Lightweight Deep Learning for EEG', { underline: true });
doc.moveDown();
doc.fontSize(12).text('This study classifies cognitive load using EEG data...');
doc.addPage();

// Page 3
doc.fontSize(20).text('2. Language Switching in Multi-linguals', { underline: true });
doc.moveDown();
doc.fontSize(12).text('This study uses multilingual BERT to model English-Spanish language switching.');
doc.addPage();

// Page 4
doc.fontSize(20).text('3. Evaluating the Robustness of Recurrent RL', { underline: true });
doc.moveDown();
doc.fontSize(12).text('This report explores the design and comparative evaluation of Deep Q-Network...');
doc.addPage();

doc.end();
console.log('Created Mini_Research_Reports.pdf');
