#gets the first testcase from each testgroup with under 1k weights, replace filepath accordingly

testgroups = ['n00050', 'n00100', 'n00200', 'n00500', 'n01000']
Rtestgroup = 'R01000'
groupnames = ['01WeaklyCorrelated','02StronglyCorrelated','03InverseStronglyCorrelated', '04AlmostStronglyCorrelated', '05SubsetSum', '06UncorrelatedWithSimilarWeights', '07SpannerUncorrelated', '08SpannerWeaklyCorrelated','09SpannerStronglyCorrelated', '10MultipleStronglyCorrelated','11ProfitCeiling', '12Circle']


import shutil
for groupname in groupnames:
    for testgroup in testgroups:
        filepath = "D:/HOC/Tri Tue Nhan Tao/KnapsackProblems/kplib-master/kplib-master/" + groupname + '/' + testgroup + '/' + Rtestgroup + '/s021.kp'
        newfilepath ="D:/HOC/Tri Tue Nhan Tao/KnapsackProblems/kplib-master/kplib-master/" + groupname + '/' + testgroup+".kp"
        shutil.move(filepath, newfilepath)