# Generated by Django 3.0.4 on 2020-08-24 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0004_auto_20200824_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thirdtable',
            name='BS_count',
        ),
        migrations.RemoveField(
            model_name='thirdtable',
            name='BTN_count',
        ),
        migrations.RemoveField(
            model_name='thirdtable',
            name='DM_count',
        ),
        migrations.RemoveField(
            model_name='thirdtable',
            name='DP_count',
        ),
        migrations.RemoveField(
            model_name='thirdtable',
            name='OWft_count',
        ),
        migrations.RemoveField(
            model_name='thirdtable',
            name='TC_count',
        ),
        migrations.RemoveField(
            model_name='thirdtable',
            name='TP_count',
        ),
        migrations.RemoveField(
            model_name='thirdtable',
            name='WDR_coun_Weavers',
        ),
        migrations.RemoveField(
            model_name='thirdtable',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='thirdtable',
            name='time_date',
        ),
        migrations.RemoveField(
            model_name='thirdtable',
            name='time_modified',
        ),
        migrations.AddField(
            model_name='thirdtable',
            name='BS_count_Machine',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thirdtable',
            name='BTN_count_Machine',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thirdtable',
            name='DM_count_Machine',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thirdtable',
            name='DP_count_Machine',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thirdtable',
            name='OWft_count_Machine',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thirdtable',
            name='TC_count_Machine',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thirdtable',
            name='TP_count_Machine',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thirdtable',
            name='WDR_count_Weavers',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='BP_count_Machine',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='CM_count_Yawn',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='COV_count_DyedYarn',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='CR_count_Machine',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='CV_count_Yawn',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='CW_count_Yawn',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='CWp_count_Yawn',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='Ctn_count_Yawn',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='DE_count_Machine',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='DOP_count_Weavers',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='EH_count_Machine',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='FL_count_Machine',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='HS_count_Weavers',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='H_count_Machine',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='LM_count_Machine',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='LO_count_Machine',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='LWP_count_Machine',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='MB_count_Machine',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='ME_count_Machine',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='OWP_count_Machine',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='RM_count_Machine',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='SEF_count_Machine',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='SM_count_Machine',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='SOS_count_Sizing',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='SPB_count_Sizing',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='SS_count_Sizing',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='STB_count_DyedYarn',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='SV_count_Sizing',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='SW_count_Weavers',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='SY_count_Yawn',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='TER_count_Machine',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='TL_count_Machine',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='TM_count_Machine',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='ThTh_count_Yawn',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='WDT_count_Weavers',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='WWft_count_Weavers',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='thirdtable',
            name='YSV_count_Yawn',
            field=models.CharField(max_length=150),
        ),
    ]
