from django import forms

class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False)
        
class SelectForm(forms.Form):
    data=[
           ('1', '横浜駅'),
           ('2', '川崎駅'),        
           ('16', '関内駅'),   
           ('17', '溝の口駅'), 
           ('18', '藤沢駅'),
           ('19', '相模大野駅'),
           ('121', '三鷹駅'),
           ('123', '大森駅'),
           ('131', '蒲田駅'),
        
        ]

    select = forms.ChoiceField(label='Choice', choices=data)    
    


















