// Created by Onur Dursun on 20.04.2022.
#ifndef CPP_01_WEAPON_HPP
#define CPP_01_WEAPON_HPP

#include <iostream>

using	std::cout;
using 	std::string;
using	std::endl;

class Weapon
{
public:
	string	getType( void );
	void	setType( string _name );
	Weapon (string _name);
private:
	string weapon_;
};

#endif //CPP_01_WEAPON_HPP
