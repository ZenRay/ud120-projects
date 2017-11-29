#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    # print type(ages), type(net_worths)

    ### your code goes here
    # print sorted(predictions)
    # print sorted(net_worths)
    # errors = [abs(predictions[i] - net_worths[i]) for i in range(len(predictions))]
    # temp = []
    # errors = []

    # for i in range(len(ages)):
    #     temp.append((ages[i], net_worths[i], net_worths[i]-predictions[i]))
    #     errors.append(net_worths[i] - predictions[i])

    # errors.sort()
    # clean_errors = errors[9:]
    # print errors[:10]

    # for i in range(len(temp)):
    #     if temp[i][2] in clean_errors:
    #         cleaned_data.append(temp[i])




    ages = list(ages)
    net_worths = list(net_worths)
    errors = []
    temp_result = []
    for prediction, net_worth, age in zip(predictions, net_worths, ages):
        errors.append(net_worth - prediction)
        temp_result.append((age, net_worth, net_worth - prediction))


    sort_errors = sorted(errors)
    # count the total of outlier
    outlier_count = int(len(ages)*.1)
    # # remove outlier
    for i in temp_result:
        if i[2] in sort_errors[outlier_count: ]:
            cleaned_data.append(i)


    # for i in range(int(len(ages)*.1)):
    #     pop_value = sort_errors.pop()
    #     # print pop_value
    #     pop_index = errors.index(pop_value)

    #     print ages[pop_index],  net_worths[pop_index], errors[pop_index], pop_value
    #     ages.remove(ages[pop_index])
    #     net_worths.remove(net_worths[pop_index])
    #     errors.remove(errors[pop_index])



    # for i in zip(ages, net_worths, errors):
    #     # print ages[i], net_worths[i], errors[i]
    #     cleaned_data.append(i)

    
    return cleaned_data

