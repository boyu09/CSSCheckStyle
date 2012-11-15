import sys
from ckstyle.doCssCheck import doCheck
from ckstyle.reporter.ReporterUtil import ReporterUtil
from ckstyle.cssparser.CssFileParser import CssParser
from ckstyle.entity.StyleSheet import StyleSheet

def checkCssFileByOpm(filePath):
    fileContent = open(filePath).read()
    checker = doCheck(fileContent, filePath)
    print checker.parser.styleSheet._ruleSets[0].comment
    if checker.hasError():
        reporter = ReporterUtil.getReporter('text', checker)
        reporter.doReport()
        print reporter.export()
        return False
    return True

if __name__ == '__main__':
    checkCssFileByOpm('test.css')
