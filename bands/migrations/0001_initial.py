# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-06 09:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('bio', models.TextField(blank=True, null=True)),
                ('start', models.IntegerField(blank=True, choices=[(None, '...'), (1955, '1955'), (1956, '1956'), (1957, '1957'), (1958, '1958'), (1959, '1959'), (1960, '1960'), (1961, '1961'), (1962, '1962'), (1963, '1963'), (1964, '1964'), (1965, '1965'), (1966, '1966'), (1967, '1967'), (1968, '1968'), (1969, '1969'), (1970, '1970'), (1971, '1971'), (1972, '1972'), (1973, '1973'), (1974, '1974'), (1975, '1975'), (1976, '1976'), (1977, '1977'), (1978, '1978'), (1979, '1979'), (1980, '1980'), (1981, '1981'), (1982, '1982'), (1983, '1983'), (1984, '1984'), (1985, '1985'), (1986, '1986'), (1987, '1987'), (1988, '1988'), (1989, '1989'), (1990, '1990'), (1991, '1991'), (1992, '1992'), (1993, '1993'), (1994, '1994'), (1995, '1995'), (1996, '1996'), (1997, '1997'), (1998, '1998'), (1999, '1999'), (2000, '2000'), (2001, '2001'), (2002, '2002'), (2003, '2003'), (2004, '2004'), (2005, '2005'), (2006, '2006'), (2007, '2007'), (2008, '2008'), (2009, '2009'), (2010, '2010'), (2011, '2011'), (2012, '2012'), (2013, '2013'), (2014, '2014'), (2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024'), (2025, '2025'), (2026, '2026')], null=True)),
                ('end', models.IntegerField(blank=True, choices=[(None, '...'), (1955, '1955'), (1956, '1956'), (1957, '1957'), (1958, '1958'), (1959, '1959'), (1960, '1960'), (1961, '1961'), (1962, '1962'), (1963, '1963'), (1964, '1964'), (1965, '1965'), (1966, '1966'), (1967, '1967'), (1968, '1968'), (1969, '1969'), (1970, '1970'), (1971, '1971'), (1972, '1972'), (1973, '1973'), (1974, '1974'), (1975, '1975'), (1976, '1976'), (1977, '1977'), (1978, '1978'), (1979, '1979'), (1980, '1980'), (1981, '1981'), (1982, '1982'), (1983, '1983'), (1984, '1984'), (1985, '1985'), (1986, '1986'), (1987, '1987'), (1988, '1988'), (1989, '1989'), (1990, '1990'), (1991, '1991'), (1992, '1992'), (1993, '1993'), (1994, '1994'), (1995, '1995'), (1996, '1996'), (1997, '1997'), (1998, '1998'), (1999, '1999'), (2000, '2000'), (2001, '2001'), (2002, '2002'), (2003, '2003'), (2004, '2004'), (2005, '2005'), (2006, '2006'), (2007, '2007'), (2008, '2008'), (2009, '2009'), (2010, '2010'), (2011, '2011'), (2012, '2012'), (2013, '2013'), (2014, '2014'), (2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024'), (2025, '2025'), (2026, '2026')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument', models.CharField(max_length=255)),
                ('start', models.IntegerField(blank=True, choices=[(None, '...'), (1955, '1955'), (1956, '1956'), (1957, '1957'), (1958, '1958'), (1959, '1959'), (1960, '1960'), (1961, '1961'), (1962, '1962'), (1963, '1963'), (1964, '1964'), (1965, '1965'), (1966, '1966'), (1967, '1967'), (1968, '1968'), (1969, '1969'), (1970, '1970'), (1971, '1971'), (1972, '1972'), (1973, '1973'), (1974, '1974'), (1975, '1975'), (1976, '1976'), (1977, '1977'), (1978, '1978'), (1979, '1979'), (1980, '1980'), (1981, '1981'), (1982, '1982'), (1983, '1983'), (1984, '1984'), (1985, '1985'), (1986, '1986'), (1987, '1987'), (1988, '1988'), (1989, '1989'), (1990, '1990'), (1991, '1991'), (1992, '1992'), (1993, '1993'), (1994, '1994'), (1995, '1995'), (1996, '1996'), (1997, '1997'), (1998, '1998'), (1999, '1999'), (2000, '2000'), (2001, '2001'), (2002, '2002'), (2003, '2003'), (2004, '2004'), (2005, '2005'), (2006, '2006'), (2007, '2007'), (2008, '2008'), (2009, '2009'), (2010, '2010'), (2011, '2011'), (2012, '2012'), (2013, '2013'), (2014, '2014'), (2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024'), (2025, '2025'), (2026, '2026')], null=True)),
                ('end', models.IntegerField(blank=True, choices=[(None, '...'), (1955, '1955'), (1956, '1956'), (1957, '1957'), (1958, '1958'), (1959, '1959'), (1960, '1960'), (1961, '1961'), (1962, '1962'), (1963, '1963'), (1964, '1964'), (1965, '1965'), (1966, '1966'), (1967, '1967'), (1968, '1968'), (1969, '1969'), (1970, '1970'), (1971, '1971'), (1972, '1972'), (1973, '1973'), (1974, '1974'), (1975, '1975'), (1976, '1976'), (1977, '1977'), (1978, '1978'), (1979, '1979'), (1980, '1980'), (1981, '1981'), (1982, '1982'), (1983, '1983'), (1984, '1984'), (1985, '1985'), (1986, '1986'), (1987, '1987'), (1988, '1988'), (1989, '1989'), (1990, '1990'), (1991, '1991'), (1992, '1992'), (1993, '1993'), (1994, '1994'), (1995, '1995'), (1996, '1996'), (1997, '1997'), (1998, '1998'), (1999, '1999'), (2000, '2000'), (2001, '2001'), (2002, '2002'), (2003, '2003'), (2004, '2004'), (2005, '2005'), (2006, '2006'), (2007, '2007'), (2008, '2008'), (2009, '2009'), (2010, '2010'), (2011, '2011'), (2012, '2012'), (2013, '2013'), (2014, '2014'), (2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024'), (2025, '2025'), (2026, '2026')], null=True)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bands.Band')),
            ],
        ),
        migrations.CreateModel(
            name='Musican',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='musican',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bands.Musican'),
        ),
        migrations.AddField(
            model_name='band',
            name='members',
            field=models.ManyToManyField(through='bands.Member', to='bands.Musican'),
        ),
    ]
