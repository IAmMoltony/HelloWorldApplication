def ParseDependencyList(DependencyListFileName):
    Dependencies = []
    with open(DependencyListFileName, 'r') as DependencyListFile:
        DependencyListFileContents: str = DependencyListFile.read()
        for Line in DependencyListFileContents.split("\n"):
            if Line.startswith('#'):
                continue
            if Line.isspace() or len(Line) == 0:
                continue
            Dependencies.append(Line)
    return Dependencies