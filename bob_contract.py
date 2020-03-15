#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:23:18 2020

@author: amin
"""



#%%
import smartpy as sp



class House_123456789(sp.Contract):


    def __init__(self,
                 house_price,
                 deposit_amount,
                 tenant_address,
                 financier_address):

        self.init(house_price = house_price,
                  equity_tenant = deposit_amount,
                  equity_financier = house_price - deposit_amount,
                  equity_crowd = 0,
                  rent_received_financier = 0,
                  rent_received_crowd = 0,
                  tenant_address = tenant_address,
                  financier_address = financier_address,
                  crowd_addresses = [],
                  crowd_equities = [],
                  crowd_rents = [])


    #%%
    
    def div(a, b):
        return sp.nat(((a * 1000000000) // b) // 1000000000)

    
    @sp.entry_point
    def tenant_rental_payment_to_financier(self, params):
        
        sp.verify(sp.sender == self.data.tenant_address)
        
        sp.if self.data.equity_financier > 0:
            self.data.rent_received_financier += abs(params.amount) * (self.data.equity_financier * 1000000 // self.data.house_price) // 1000000

            
    @sp.entry_point
    def tenant_rental_payment_to_crowd(self, params):
        sp.if self.data.equity_crowd > 0:
            self.data.rent_received_crowd += abs(params.amount) * (self.data.equity_crowd * 1000000 // self.data.house_price) // 1000000


    @sp.entry_point
    def tenant_rental_payment_to_all_crowd(self, params):

        sp.if self.data.equity_crowd > 0:
            self.data.rent_received_crowd += abs(params.amount) * (self.data.equity_crowd * 1000000 // self.data.house_price) // 1000000

            self.data.crowd_equities = self.data.crowd_equities.rev()

            sp.for each_equity in self.data.crowd_equities:
                self.data.crowd_rents.push(((each_equity * 1000000000) // self.data.house_price) // (100000000))

            #sp.for i in sp.range(0, sp.len(self.data.crowd_equities)):
            #    self.data.crowd_rents[i] += i+7

            self.data.crowd_equities = self.data.crowd_equities.rev()


    @sp.entry_point
    def tenant_rental_payment_to_everyone(self, params):
        sp.if self.data.equity_financier > 0:
            self.data.rent_received_financier += abs(params.amount) * (self.data.equity_financier * 1000000 // self.data.house_price) // 1000000
        sp.if self.data.equity_crowd > 0:
            self.data.rent_received_crowd += abs(params.amount) * (self.data.equity_crowd * 1000000 // self.data.house_price) // 1000000

    #%%

    @sp.entry_point
    def equity_from_financier_to_tenant(self, params):
        self.data.equity_tenant += params.amount
        sp.if self.data.equity_financier >= params.amount:
            self.data.equity_financier = abs(self.data.equity_financier - params.amount)


    @sp.entry_point
    def equity_from_financier_to_crowd(self, params):
        sp.if self.data.equity_financier >= params.amount:
            self.data.equity_crowd += params.amount
            self.data.equity_financier = abs(self.data.equity_financier - params.amount)


    @sp.entry_point
    def equity_from_crowd_to_tenant(self, params):
        sp.if self.data.equity_crowd >= params.amount:
            self.data.equity_tenant += params.amount
            self.data.equity_crowd = abs(self.data.equity_crowd - params.amount)

    #%%

    @sp.entry_point
    def add_new_crowd_address(self, params):
        self.data.crowd_addresses.push(sp.sender)
        self.data.crowd_equities.push(params.acquisition)
        self.data.crowd_rents.push(0)
        self.data.equity_crowd += params.acquisition
        self.data.equity_financier = sp.as_nat(self.data.equity_financier - params.acquisition)

    #%%



@sp.add_test(name="testingposting")
def test():
    scenario = sp.test_scenario()
    scenario.h1("Test")

    tenant_address = sp.address("tz1")
    financier_address = sp.address("tz2")
    crowd_address_1 = sp.address("tz1c")
    crowd_address_2 = sp.address("tz2c")
    crowd_address_3 = sp.address("tz3c")


    contract = House_123456789(house_price=200000,
                               deposit_amount=30000,
                               tenant_address=tenant_address,
                               financier_address=financier_address)

    scenario += contract


    test_purchases=True
    test_rents = True
    test_crowd_sale = True


    if test_purchases == True:

        scenario.h2("tenant buys from financier")
        scenario += contract.equity_from_financier_to_tenant(amount=abs(1000)).run(sender=tenant_address)

        scenario.h2("crowd buys from financier")
        scenario += contract.equity_from_financier_to_crowd(amount=abs(2000)).run(sender=tenant_address)

        scenario.h2("tenant buys from crowd")
        scenario += contract.equity_from_crowd_to_tenant(amount=abs(1000)).run(sender=tenant_address)


    if test_rents == True:

        scenario.h2("tenant pays rent to financier")
        scenario += contract.tenant_rental_payment_to_financier(amount=abs(1000)).run(sender=tenant_address)

        scenario.h2("tenant pays rent to crowd")
        scenario += contract.tenant_rental_payment_to_crowd(amount=abs(1000)).run(sender=tenant_address)

        scenario.h2("tenant pays rent to everyone")
        scenario += contract.tenant_rental_payment_to_everyone(amount=abs(1000)).run(sender=tenant_address)


    if test_crowd_sale == True:
        scenario.h2("random person 1 buys some house")
        scenario += contract.add_new_crowd_address(acquisition=2000).run(sender=crowd_address_1)
        scenario.h2("random person 2 buys some house")
        scenario += contract.add_new_crowd_address(acquisition=7000).run(sender=crowd_address_2)
        scenario.h2("random person 3 buys some house")
        scenario += contract.add_new_crowd_address(acquisition=4000).run(sender=crowd_address_3)
        
    scenario.h2("tenant pays rent to all crowd")
    scenario += contract.tenant_rental_payment_to_all_crowd(amount=10000).run(sender=tenant_address)
    
    

