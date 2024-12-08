--transfer parallel processed results

select distinct bound from psp_base_bundles order by CAST(bound as integer) desc;
select distinct bound from pspdb7.psp_base_bundles;


insert into psp_base_bundles select * from pspdb1.psp_base_bundles;
insert into psp_base_bundles select * from pspdb2.psp_base_bundles;
insert into psp_base_bundles select * from pspdb3.psp_base_bundles;
insert into psp_base_bundles select * from pspdb4.psp_base_bundles;
insert into psp_base_bundles select * from pspdb5.psp_base_bundles;
insert into psp_base_bundles select * from pspdb6.psp_base_bundles;
insert into psp_base_bundles select * from pspdb7.psp_base_bundles;
insert into psp_base_bundles select * from pspdb8.psp_base_bundles;
insert into psp_base_bundles select * from pspdb9.psp_base_bundles;
insert into psp_base_bundles select * from pspdb10.psp_base_bundles;
--insert into psp_base_bundles select * from pspdb11.psp_base_bundles;

select distinct bound from psp order by CAST(bound as integer) desc;

insert into psp select * from pspdb1.psp;
insert into psp select * from pspdb2.psp;
insert into psp select * from pspdb3.psp;
insert into psp select * from pspdb4.psp;
insert into psp select * from pspdb5.psp;
insert into psp select * from pspdb6.psp;
insert into psp select * from pspdb7.psp;
insert into psp select * from pspdb8.psp;
insert into psp select * from pspdb9.psp;
insert into psp select * from pspdb10.psp;
--insert into psp select * from pspdb11.psp;


select distinct (val / 100000000000 ) lead from spsp order by lead desc;

insert into spsp select * from pspdb1.spsp;
insert into spsp select * from pspdb2.spsp;
insert into spsp select * from pspdb3.spsp;
insert into spsp select * from pspdb4.spsp;
insert into spsp select * from pspdb5.spsp;
insert into spsp select * from pspdb6.spsp;
insert into spsp select * from pspdb7.spsp;
insert into spsp select * from pspdb8.spsp;
insert into spsp select * from pspdb9.spsp;
insert into spsp select * from pspdb10.spsp;
--insert into spsp select * from pspdb11.spsp;


