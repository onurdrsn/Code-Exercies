// Created by Onur Dursun on 20.04.2022.
#include "HumanA.hpp"

HumanA::HumanA( std::string name, Weapon &weapon ): name(name), weapon(weapon)
{
}

void	HumanA::attack () {
	if (weaponType)
		cout << name << " attacks with his " << weapon.getType() << endl;
	else
		cout << name <<  " can't attack because they don't have a weapon" << endl;
}
Weapon &HumanA::getWeapon( void ) const
{
	return  (weapon);
}
#include "HumanA.hpp"
