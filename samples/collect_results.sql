ATTACH '../data/pseudo_prime.db' as master;

delete from spsp;
delete from psp;
delete from psp_base_bundles;

insert into psp_base_bundles
select * from master.psp_base_bundles order by val desc LIMIT 500;

insert into psp
select * from master.psp order by val desc LIMIT 500;

insert into spsp
select * from master.spsp order by val desc LIMIT 500;
